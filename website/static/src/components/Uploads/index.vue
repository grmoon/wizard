<template>
  <div>
    <form @submit.prevent="form_onSubmit">
      <select
        v-model="command"
        required
      >
        <option
          disabled
          selected
          value=""
        >
          Select an Action:
        </option>
        <option value="delete">
          Delete
        </option>
      </select>
      <input
        type="submit"
        value="Go"
      >
    </form>
    <table>
      <thead>
        <tr>
          <th>Filename</th>
          <th>Created At</th>
          <th>
            <input
              ref="selectAll"
              type="checkbox"
              :name="uuid"
              @click="selectAll_onClick"
            >
          </th>
        </tr>
      </thead>
      <tbody ref="body">
        <tr
          v-for="(upload, index) in uploads"
          :key="index"
        >
          <td>
            <a
              download
              :href="upload.file"
            >{{ getFilename(upload.file) }}</a>
          </td>
          <td>{{ formatDate(upload.created_at) }}</td>
          <td>
            <input
              type="checkbox"
              :name="uuid"
              :value="upload.id"
              @click="checkbox_onClick"
            >
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { v4 as uuid } from 'uuid';
import { mapActions } from 'vuex';
import moment from 'moment';
const _moment = moment;

export default {
    props: {
        uploads: {
            required: true,
            type: Array
        }
    },
    data() {
        return {
            command: '',
            uuid: uuid(),
        };
    },
    computed: {
        checkboxes() {
            return Array.from(this.$refs.body.querySelectorAll(`input[type='checkbox'][name='${this.uuid}']`));
        },
        checkedCheckboxes() {
            return this.checkboxes.filter(checkbox => checkbox.checked);
        }
    },
    methods: {
        ...mapActions(['deleteUploads']),
        formatDate(rawDate) {
          const format = 'dddd, MMMM Do YYYY, h:mm:ss a';
          return moment(rawDate).format(format);
        },
        form_onSubmit() {
            const ids = this.checkedCheckboxes.map(checkbox => checkbox.value);

            const handlers = {
                delete: this.deleteUploads
            }

            return handlers[this.command](ids);
        },
        getFilename(path) {
            return path.split('/').slice(-1).pop();
        },
        checkbox_onClick() {
            this.$refs.selectAll.checked = false;
        },
        selectAll_onClick(event) {
            this.checkboxes.forEach((checkbox) => {
                checkbox.checked = event.currentTarget.checked;
            });
        }
    }
}
</script>