// router.js

import SiteContainer from '../components/SiteContainer';
import {createRouter, createWebHistory} from "vue-router/dist/vue-router";
import AuthPage from "@/components/AuthPage";

const routes = [
  {
    path: '/',
    name: 'SiteContainer',
    component: SiteContainer,
  },
  {
    path: '/login',
    name: 'AuthPage',
    component: AuthPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;


