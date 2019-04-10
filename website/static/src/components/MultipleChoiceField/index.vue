<template>
  <component
    :is="component"
    :answer="answer"
    :field="field"
    :options="options"
  />
</template>

<script>
import CheckboxField from '@components/CheckboxField';
import SelectField from '@components/SelectField';
import RadioButtonField from '@components/RadioButtonField';
import sortByPosition from '@utils/sortByPosition';
import { mapState } from 'vuex';

export default {
    props: {
        field: {
            required: true,
            type: Object
        },
        answer: {
            required: true,
            type: Object
        }
    },
    computed: {
        ...mapState({
            options({ multipleChoiceOptions, options }) {
                const _options = this.field.options.reduce((acc, optionId) => {
                    const multipleChoiceOption = multipleChoiceOptions[this.field.id][optionId];
                    const option = options[optionId];

                    const augmentedOption = {
                        ...multipleChoiceOption,
                        option
                    }

                    acc.push(augmentedOption);

                    return acc;
                }, []);

                _options.sort(sortByPosition);

                return _options;
            }
        }),
        component() {
            return {
                'CheckboxField': CheckboxField,
                'RadioButtonField': RadioButtonField,
                'SelectField': SelectField,
            }[this.field.class]
        }
    }
};
</script>