import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../views/HomeView.vue'),
    },
    {
      path: '/products',
      name: 'ProductList',
      component: () => import('../views/ProductListView.vue'),
    },
    {
      path: '/product/:id',
      name: 'Product',
      component: () => import('../views/ProductView.vue'),
    },
    {
      path: '/cart',
      name: 'Cart',
      component: () => import('../views/CartView.vue'),
    },
    {
      path: '/checkout',
      name: 'Podsumowanie',
      component: () => import('@/views/CheckoutView.vue'),
    },
    {
      path: '/orderSummary',
      name: 'StatusZamówienia',
      component: () => import('@/views/orderSummaryView.vue'),
    },
    {
      path: '/account',
      name: 'Account',
      component: () => import('../views/AccountView.vue'),
      meta: { requiresAuth: true }, 
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue'),
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import('../views/RegisterView.vue'),
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import('../views/NotFoundView.vue'),
    },
    {
      path: '/admin',
      component: () => import('../views/admin/AdminPanel.vue'),
      // meta: { requiresAuth: true },
      children: [
        {
          path: 'products',
          name: 'AdminProducts',
          component: () => import('../views/admin/AdminProductList.vue'),
        },
        {
          path: 'customers',
          name: 'AdminCustomers',
          component: () => import('../views/admin/AdminCustomerList.vue'),
        },
        {
          path: '/admin/stats',
          name: 'AdminStats',
          component: () => import('../views/admin/AdminStats.vue'),
        }
      ],
    },
  ],
});


// Navigation Guard for protected routes
// router.beforeEach((to, from, next) => {
//   if (to.meta.requiresAuth) {
//     const token = localStorage.getItem('jwt');
//     if (token) {
//       // Opcjonalnie: można dodać weryfikację tokena, np. sprawdzając datę wygaśnięcia
//       next();
//     } else {
//       alert('Zaloguj się aby otworzyć tą stronę ');
//       next({ name: 'Login' });
//     }
//   } else {
//     next();
//   }
// });

export default router
