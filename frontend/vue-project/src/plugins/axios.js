import axios from 'axios';
import { BASE_URL } from '@/main';

const instance =  axios.create({
    baseURL: `${BASE_URL}`,
    timeout: 5000,
  });

instance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('jwt');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default instance;