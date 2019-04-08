import Vue from 'vue';
import VueRouter from 'vue-router';
import WizardController from '@components/WizardController';
import Done from '@components/Done';

Vue.use(VueRouter);

export default new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/wizard/:wizardId/step/:stepNum/',
            component: WizardController,
            name: 'wizard',
            pathToRegexpOptions: { strict: true },
        },
        {
            path: '/done/',
            component: Done,
            name: 'done',
            pathToRegexpOptions: { strict: true },
        }
    ]
});