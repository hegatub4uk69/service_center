<template>
  <v-card class="fill-height">
    <v-container>
      <v-row align="center" justify="center" dense="">
        <v-col cols="12" sm="8" md="4" lg="6">
          <v-row align="center" justify="center" dense="">
            <v-avatar image="/kompyuternyj-servis.png" size="300px"/>
          </v-row>
          <v-row align="center" justify="center" dense="" class="justify-center pb-5">
            <span class="title text-secondary py-2 font-weight-bold">{{ name }}</span>
          </v-row>
          <v-text-field
            label="First Name"
            prepend-inner-icon="mdi-account-outline"
          ></v-text-field>
          <v-text-field
            label="Last Name"
            prepend-inner-icon="mdi-account-outline"
          ></v-text-field>
          <v-text-field
            label="Username"
            prepend-inner-icon="mdi-account-outline"
          ></v-text-field>
          <v-text-field
            label="Email"
            prepend-inner-icon="mdi-email-outline"
          ></v-text-field>
          <v-text-field
            label="Address"
            prepend-inner-icon="mdi-map-marker-outline"
          ></v-text-field>
          <v-text-field
            label="Phone Number"
            prepend-inner-icon="mdi-phone-outline"
          ></v-text-field>
          <v-row>
            <v-col cols="12" md="6">
              <v-btn
                color="secondary"
                text
                block
                tile
                elevation="0"
                class="pa-6 font-weight-bold"
              >Cancel
              </v-btn>
            </v-col>
            <v-col cols="12" md="6">
              <v-btn
                color="info"
                class="pa-6 font-weight-bold"
                block
                tile
                elevation="0"
              >Update
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'ProfilePage',
};
</script>
