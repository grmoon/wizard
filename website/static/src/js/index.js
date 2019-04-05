import App from '@components/App';
import Vue from 'vue';
import store from '@js/store';

new Vue({
    el: '#app',
    store,
    render(createElement) {
        return createElement(App);
    }
})