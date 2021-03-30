<template>
  <div id="container">
    <v-stepper v-model="e1">
      <v-stepper-header>
        <v-stepper-step :complete="e1 > 1" editable step="1" color="#6A1B9A">
          step 1
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="e1 > 2" editable step="2" color="#6A1B9A">
          step 2
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3" editable color="#6A1B9A">
          step 3
        </v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <FirstOption></FirstOption>

          <v-row justify="end">
            <v-btn class="ma-4" color="#EDE7F6" @click="e1 = 2">
              <span class="ts">다음</span>
            </v-btn>
          </v-row>
        </v-stepper-content>

        <v-stepper-content step="2">
          <SecondOption></SecondOption>

          <v-row justify="end">
            <v-btn class="mt-4 mb-4 mr-4" color="#EDE7F6" @click="e1 = 1">
              <span class="ts">이전</span>
            </v-btn>

            <v-btn class="mt-4 mb-4 mr-4" color="#EDE7F6" @click="e1 = 3">
              <span class="ts">다음</span>
            </v-btn>
          </v-row>
        </v-stepper-content>

        <v-stepper-content step="3">
          <ThirdOption></ThirdOption>

          <v-row justify="end">
            <v-btn class="mt-4 mb-4 mr-4" color="#EDE7F6" @click="e1 = 2">
              <span class="ts">이전</span>
            </v-btn>

            <v-btn class="mt-4 mb-4 mr-4" color="#EDE7F6" @click="moveToTravelingCourse">
              <span class="ts">코스 추천 받기</span>
            </v-btn>
          </v-row>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>

<script>
import FirstOption from "@/components/courses/FirstOption.vue";
import SecondOption from "@/components/courses/SecondOption.vue";
import ThirdOption from "@/components/courses/ThirdOption.vue";

export default {
  name: "SelectOption",
  components: {
    FirstOption,
    SecondOption,
    ThirdOption,
  },
  data() {
    return {
      e1: 1,
    };
  },
  methods: {
    moveToTravelingCourse() {
      console.log("여행코스로 이동");
      this.$router.push({ name: "TravelingCourse" });
    },
  },
};
</script>

<style scoped>
.ts {
  color: #6A1B9A;
  font-weight: 900;
}
</style>
