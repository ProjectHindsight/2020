import Vue from 'vue';
import VueRouter from 'vue-router';
import Question from '../components/Question.vue';
import Books from '../components/Books.vue';
import Ping from '../components/Ping.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'q',
    component: Question,
  },
  {
    path: '/books',
    name: 'Books',
    component: Books,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
