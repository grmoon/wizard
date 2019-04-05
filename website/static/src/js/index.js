import App from '@components/App';
import Vue from 'vue';

new Vue({
    el: '#app',
    render(createElement) {
        return createElement(App);
    }
})