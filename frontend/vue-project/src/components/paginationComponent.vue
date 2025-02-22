<v-pagination
          v-model="currentPage"
          :length="totalPages"
          @update:model-value="fetchProducts"
        ></v-pagination>