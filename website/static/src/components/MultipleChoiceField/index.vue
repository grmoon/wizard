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
import { mapState } from 'vuex';

export default {
    computed: {
        ...mapState({
            options({ multipleChoiceFieldOptions, options }) {
                const _multipleChoiceFieldOptions = {};
                const _options = this.field.options.reduce((acc, multipleChoiceFieldOptionId) => {
                    const multipleChoiceFieldOption = multipleChoiceFieldOptions[multipleChoiceFieldOptionId];
                    const optionId = multipleChoiceFieldOption.option;
                    const option = options[optionId];

                    _multipleChoiceFieldOptions[optionId] = multipleChoiceFieldOption;
                    acc.push(option);

                    return acc;
                }, []);

                _options.sort((option1, option2) => {
                    const pos1 = _multipleChoiceFieldOptions[option1.id].position;
                    const pos2 = _multipleChoiceFieldOptions[option2.id].position;

                    return pos1 - pos2;
                });

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