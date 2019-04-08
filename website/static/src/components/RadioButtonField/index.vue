<template>
  <div>
    <RadioButtonOption
      v-for="(option, index) in options"
      :key="index"
      :name="field.uuid"
      :option="option.option"
      :answer="answer"
    />
  </div>
</template>

<script>
import RadioButtonOption from '@components/RadioButtonOption';

export default {
    components: { RadioButtonOption },
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
    }
};
</script>