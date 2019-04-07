<template>
    <div>
        <RadioButtonOption
            v-for='(option, index) in options'
            :key='index'
            :name='field.name'
            :option='option'
            :answer='answer'
        />
    </div>
</template>

<script>
import axios from 'axios';
import RadioButtonOption from '@components/RadioButtonOption';
import sortByPosition from '@utils/sortByPosition';
import { mapState } from 'vuex';

export default {
    components: { RadioButtonOption },
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
        })
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