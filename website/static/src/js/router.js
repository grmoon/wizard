import Vue from 'vue';
import VueRouter from 'vue-router';
import WizardController from '@components/WizardController';

Vue.use(VueRouter);

export default new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/wizard/:wizardId/step/:stepNum/',
            component: WizardController,
            name: 'wizard',
            pathToRegexpOptions: { strict: true },
        }
    ]
});