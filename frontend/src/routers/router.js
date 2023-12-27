// router.js

import SiteContainer from '../components/SiteContainer';
import LoginPage from '../components/LoginPage';
import {createRouter, createWebHistory} from "vue-router/dist/vue-router";

const routes = [
  {
    path: '/',
    name: 'SiteContainer',
    component: SiteContainer,
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;


