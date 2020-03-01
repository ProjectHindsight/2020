import Vue from 'vue';
import VueRouter from 'vue-router';
import Books from '../components/Books.vue';
import Ping from '../components/Ping.vue';
import MoodTracker from '../components/MoodTracker.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Books',
    component: Books,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/mood_tracker',
    name: 'Mood Tracker',
    component: MoodTracker,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
