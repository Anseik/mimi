<template>
  <div id="map" class="map-container" style="width:400px;height:400px;"></div>
</template>

<script>
export default {
  name: 'RestaurantDetailMap',
  async mounted() {
    var mapContainer = document.getElementById('map'),
        mapOption = { 
            center: new window.kakao.maps.LatLng(33.450701, 126.570667),
            level: 3
        };

    var map = new window.kakao.maps.Map(mapContainer, mapOption);

    var markerPosition  = new window.kakao.maps.LatLng(33.450701, 126.570667); 

    const imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
    const imageSize = new window.kakao.maps.Size(24, 35);
    const markerImage = new window.kakao.maps.MarkerImage(imageSrc, imageSize);

    var marker = new window.kakao.maps.Marker({
        position: markerPosition,
        image : markerImage
    });

    marker.setMap(map);
    
  }
}
</script>

<style>
.map-container {
  display: flex;
  justify-content: center;
  margin-bottom: 5px;
  margin-left: auto;
  margin-right: auto;
}
</style>