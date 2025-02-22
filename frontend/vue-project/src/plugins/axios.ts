import axios from 'axios';

export const BASE_URL: string = 'http://localhost:8001'

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