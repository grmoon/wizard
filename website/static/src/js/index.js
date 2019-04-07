import App from '@components/App';
import Vue from 'vue';
import store from '@js/store';
import router from '@js/router';

new Vue({
    el: '#app',
    store,
    router,
    render(createElement) {
        return createElement(App);
    }
})