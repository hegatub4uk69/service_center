<template>
  <v-app>

    <v-app-bar
      app
      color="primary"
      theme="dark"
      image="https://www.fonstola.ru/images/201111/fonstola.ru_52146.jpg"
    >
      <v-app-bar-title>
        <h3 class="text-h4 white--text">{{ app_name }}</h3>
      </v-app-bar-title>
    </v-app-bar>

    <v-navigation-drawer
      image="https://www.fonstola.ru/images/201111/fonstola.ru_52146.jpg"
      permanent="" expand-on-hover="" rail="">
      <v-list>
        <v-list-item
          prepend-avatar="/kompyuternyj-servis.png"
          :title="user.fullName"
          :subtitle="user.email"
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
          :to="links.login"
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-archive-outline"
          :title="nav_menu.btn_services"
          value="archive">
        </v-list-item>
        <v-list-item
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-card-plus-outline"
          :title="nav_menu.btn_reg_serv"
          value="new_serv">
        </v-list-item>
        <v-list-item
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-logout"
          :title="nav_menu.btn_logout"
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
export default {
  name: 'App',
  data: () => ({
    app_name: 'Сервисный центр',
    user: {
      fullName: 'Test Test',
      email: 'test@gmail.com'
    },
    nav_menu: {
      btn_lk: 'Личный кабинет',
      btn_services: 'Архив услуг',
      btn_reg_serv: 'Оформление услуги',
      btn_logout: 'Выход',
    },
    links: {
      main: '/',
      login: '/login',
      profile: '/profile',
    },
  }),
}
</script>
