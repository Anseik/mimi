<template>
  <div>
    <v-container fluid class="backcolor">
      <v-simple-table dense>
        <template v-slot:default>
          <tbody>
            <tr>
              <th style="width: 100px">
                <v-img
                  :src="placeItem.image"
                  @click.stop="dialog1 = true"
                  style="width: 100px; border-radius: 20px;"
                ></v-img>
                <v-dialog v-model="dialog1" width="80%">
                  <v-card>
                    <PlaceModal :placeModal="placeItem"></PlaceModal>
                  </v-card>
                </v-dialog>
              </th>
              <th class="text-left">
                <p @click.stop="dialog1 = true">
                  {{ placeItem.title }}<br />
                  {{ placeItem.telephone }}<br />
                  {{ placeItem.address }}<br />
                </p>

                <v-dialog v-model="dialog1" width="80%">
                  <v-card>
                    <PlaceModal :placeModal="placeItem"></PlaceModal>
                  </v-card>
                </v-dialog>
              </th>
              <th class="text-right" style="width: 5px">
                <v-dialog v-model="dialog" max-width="290">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      fab
                      dark
                      small
                      color="indigo"
                      v-bind="attrs"
                      v-on="on"
                    >
                      <v-icon dark>
                        mdi-plus
                      </v-icon>
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title>음식점을 저장하세요.</v-card-title>
                    <p>해당날짜</p>
                    <v-divider></v-divider>
                    <v-card-text style="height: 100px;">
                      <v-radio-group v-model="dialogm1">
                        <v-radio label="아침" value="breakfast"></v-radio>
                        <v-radio label="점심" value="lunch"></v-radio>
                        <v-radio label="저녁" value="dinner"></v-radio>
                      </v-radio-group>
                    </v-card-text>
                    <v-card-actions>
                      <v-btn color="black" text @click="dialog = false">
                        닫기
                      </v-btn>
                      <v-btn color="black" text @click="dialog = false">
                        저장
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </th>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-container>
    <div style="line-height:50%;">
      <br />
    </div>
  </div>
</template>

<script>
import PlaceModal from "@/components/courses/PlaceModal.vue";
export default {
  name: "RestaurantItem",
  components: {
    PlaceModal,
  },
  props: {
    placeItem: Object,
  },
  data() {
    return {
      dialogm1: "",
      dialog: false,
      dialog1: false,
    };
  },
  // methods: {
  //   RestaurantDetail() {
  //     this.$router.push({ name: 'RestaurantDetail' })
  //   },

  // }
};
</script>

<style scoped>
.backcolor {
  background-color: white;
  border-radius: 20px;
}
</style>
