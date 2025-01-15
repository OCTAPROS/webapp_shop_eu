import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/products',
      name: 'products',
      component: () => import('../views/ProductListView.vue')
    },
    {
      path: '/cart',
      name: 'cart',
      component: () => import('../views/CartView.vue'),
      meta: { requiresAuth: true },
    },
    { 
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue')
    },
    { 
      path: '/register',
      name: 'Register',
      component: () => import('../views/RegisterView.vue')
    },
  ]
})

// Navigation Guard for protected routes
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    const token = localStorage.getItem('jwt');
    if (token) {
      // Opcjonalnie: można dodać weryfikację tokena, np. sprawdzając datę wygaśnięcia
      next();
    } else {
      alert('Zaloguj się aby otworzyć tą stronę ');
      next({ name: 'Login' });
    }
  } else {
    next();
  }
});

export default router
