<template>
  <select
    :autocomplete="field.autocomplete"
    :autofocus="field.autofocus"
    :disabled="field.disabled"
    :multiple="field.multiple"
    :name="field.uuid"
    :required="field.required"
    :size="field.size"
    @change="select_onChange"
  >
    <SelectOption
      v-for="(option, index) in options"
      :key="index"
      :option="option.option"
      :selected="isSelected(option.option)"
    />
  </select>
</template>

<script>
import SelectOption from '@components/SelectOption';
import { mapMutations } from 'vuex'

export default {
    components: { SelectOption },
    props: {
        answer: {
            required: true,
            type: Object
        },
        field: {
            required: true,
            type: Object
        },
        options: {
            required: true,
            type: Array
        },
    },
    computed: {
        answerValue() {
          let value;

          if (this.field.multiple) {
            value = this.getMultipleFieldAnswerValue();
          }
          else {
            value = this.getSingleAnswerValue();
          }

          return value;
      },
    },
    methods: {
      ...mapMutations(['setAnswerValue']),
      getSingleAnswerValue() {
          let value;

          if (Array.isArray(this.answer.value)) {
            value = this.answer.value[0] || null;
          }
          else {
            value = this.answer.value;
          }

          return value;
      },
      getMultipleFieldAnswerValue() {
        let value;

        if (Array.isArray(this.answer.value)) {
          value = this.answer.value;
        }
        else {
          value = this.getArrayizedAnswerValue();
        }

        return value;
      },
      getArrayizedAnswerValue() {
        let value;

        if (this.answer.value === null) {
          value = [];
        }
        else {
          value = [this.answer.value];
        }

        return value;
      },
      isSelected(option) {
        let selected;

        if (this.field.multiple) {
          selected = this.answerValue.includes(option.value);
        }
        else {
          selected = this.answerValue == option.value;
        }

        return selected;
      },
      select_onChange(event) {
        let value;

        if (this.field.multiple) {
          value = Array.from(event.currentTarget.selectedOptions).map(option => option.value);
        }
        else {
          value = event.currentTarget.value;
        }

        this.setAnswerValue({
            questionId: this.answer.question,
            value
        });
      }
    }
};
</script>