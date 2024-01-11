<template>
  <v-app>

    <v-app-bar
      app
      color="primary"
    >
      <template v-slot:prepend>
        <v-avatar
          size="54"
          rounded="0"
        >
          <v-img src="/komp-servis.png"></v-img>
        </v-avatar>
      </template>
      <v-app-bar-title>
        <h3 class="text-h4 white--text">{{ app_name }}</h3>
      </v-app-bar-title>
    </v-app-bar>

    <v-navigation-drawer
      v-if="accessToken != null"
      image="https://img3.akspic.ru/crops/1/9/6/3/1/113691/113691-sinij_cvet-lazur-svet-geometricheskaya_forma-atmosfera-2048x1152.jpg"
      permanent="" expand-on-hover="" rail="">
      <v-list>
        <v-list-item
          base-color="white"
          prepend-avatar="/free-icon-avatar-8727604.png"
          :title="user_data.staff_full_name"
          :subtitle="user_data.staff_phone"
        ></v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list density="compact" nav="">
        <v-list-item
          :to="links.profile"
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-account-circle-outline"
          :title="nav_menu.btn_lk"
          value="lk">
        </v-list-item>
        <v-list-item
          v-if="user_data.post === 'Администратор'"
          :to="links.admin"
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-cog-box"
          :title="nav_menu.btn_admin"
          value="adm_panel">
        </v-list-item>
        <v-list-item
          :to="links.orders"
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-checkbook"
          :title="nav_menu.btn_services"
          value="archive">
        </v-list-item>
        <v-list-item
          :to="links.clients"
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-account-multiple-plus-outline"
          :title="nav_menu.btn_clients"
          value="new_order">
        </v-list-item>
        <v-list-item
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-logout"
          :title="nav_menu.btn_logout"
          @click="logout"
          value="logout">
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
import router from "@/router";
import {mapState} from "vuex";
import API from "@/axios";
import {createToast} from "mosha-vue-toastify";
import 'mosha-vue-toastify/dist/style.css'

export default {
  name: 'App',
  computed: mapState(['accessToken', 'user_data']),

  data: () => ({
    app_name: 'Сервисный центр',
    user: {
      fullName: 'Test Test',
      phone: 'test@gmail.com'
    },
    nav_menu: {
      btn_lk: 'Личный кабинет',
      btn_admin: 'Панель администратора',
      btn_services: 'Заказы',
      btn_clients: 'Клиенты',
      btn_logout: 'Выход',
    },
    links: {
      main: '/',
      log: '/login',
      profile: '/profile',
      orders: '/orders',
      clients: '/clients',
      admin: '/admin'
    },
  }),

  created() {
    API.interceptors.response.use(
      response => response,
      error => {
        if (error) {
          router.push({name: 'login'})
          this.$store.dispatch('userLogout').then(
            createToast('Неверные аутентификационные данные!', {
              showIcon: 'true',
              showCloseButton: false,
              type: 'danger',
              position: "top-center",
              timeout: 3000,
              toastBackgroundColor: '#ff5252'
            })
          )
        }
      });
  },
  mounted() {
    if (!this.$store.getters.staffDataExist) {
      this.staffData()
    }
  },

  methods: {
    staffData() {
      this.$store.dispatch('userData')
    },
    logout() {
      this.$store.dispatch('userLogout')
        .then(() => {
          router.push({name: 'login'})
          window.location.reload()
        })
        .catch(err => {
          router.push({name: 'login'})
          console.log(err)
        })
    }
  }
}
</script>
