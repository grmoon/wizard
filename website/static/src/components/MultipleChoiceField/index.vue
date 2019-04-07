<template>
    <component
        :answer='answer'
        :field='field'
        :options='options'
        :is='component'
    />
</template>

<script>
import CheckboxField from '@components/CheckboxField';
import RadioButtonField from '@components/RadioButtonField';
import sortByPosition from '@utils/sortByPosition';
import { mapState } from 'vuex';

export default {
    computed: {
        ...mapState({
            options({ multipleChoiceFieldOptions, options }) {
                const _options = this.field.options.reduce((acc, multipleChoiceFieldOptionId) => {
                    const multipleChoiceFieldOption = multipleChoiceFieldOptions[multipleChoiceFieldOptionId];
                    const option = options[multipleChoiceFieldOption.option];

                    const augmentedOption = {
                        ...multipleChoiceFieldOption,
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
            }[this.field.class]
        }
    },
    props: {
        field: {
            required: true,
            type: Object
        },
        answer: {
            required: true,
            type: Object
        }
    }
};
</script>