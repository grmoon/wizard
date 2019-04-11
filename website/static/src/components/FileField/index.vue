<template>
  <div>
    <div v-if="uploads.length > 0">
      Currently Selected {{ uploads.length > 1 ? 'Files' : 'File' }}:
      <Uploads :uploads="uploads" />
    </div>
    <input
      type="file"
      :accept="field.accept"
      :multiple="field.multiple"
      :required="field.required"
      @change="input_onChange"
    >
  </div>
</template>

<script>
import Uploads from '@components/Uploads'
import { mapMutations, mapState } from 'vuex';

export default {
  components: { Uploads },
    props: {
        answer: {
            required: true,
            type: Object
        },
        field: {
            required: true,
            type: Object
        }
    },
    computed: mapState({
        uploads({ uploads }) {
            return uploads[this.answer.id] || [];
        }
    }),
    methods: {
        ...mapMutations(['setAnswerValue']),
        input_onChange(event) {
            this.setAnswerValue({
                questionId: this.answer.question,
                value: event.currentTarget.files
            });
        }
    }
}
</script>