<template>
  <div>
    <CheckboxOption
      v-for="(option, index) in options"
      :key="index"
      :name="field.uuid"
      :option="option"
      :answer="answer"
      :exclusive-values="exclusiveValues"
    />
  </div>
</template>

<script>
import CheckboxOption from '@components/CheckboxOption';

export default {
    components: { CheckboxOption },
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
        exclusiveValues() {
            return this.options.reduce((acc, option) => {
                if (option.exclusive) {
                    acc.push(option.option.value)
                }

                return acc
            }, []);
        }
    }
};
</script>