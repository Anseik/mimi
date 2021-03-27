<template>
  <div id="map" class="map-container" style="width:400px;height:200px;"></div>
</template>

<script>
export default {
    name: 'CourseMap',
    async mounted() {
        var container = document.getElementById('map');
        var options = {
            center: new window.kakao.maps.LatLng(36.10253216664124, 128.41969978161438),
            level: 3
        };

        var map = new window.kakao.maps.Map(container, options);
        console.log(map);

        var linePath = [
            new window.kakao.maps.LatLng(36.10295116992656, 128.4197017694798),
            new window.kakao.maps.LatLng(36.10193335258725, 128.419852793029),
            new window.kakao.maps.LatLng(36.101736905882, 128.4195105805213),
        ];

        var polyline = new window.kakao.maps.Polyline({
            path: linePath, // 선을 구성하는 좌표배열
            strokeWeight: 5, // 선의 두께
            strokeColor: '#356859', // 선의 색깔
            strokeOpacity: 0.7, // 선의 불투명 - 1에서 0 사이의 값이며 0에 가까울수록 투명
            strokeStyle: 'solid' // 선의 스타일
        });

        polyline.setMap(map); 

        var positions = [
            {
                title: '유리네', 
                latlng: new window.kakao.maps.LatLng(36.101736905882, 128.4195105805213)
            },
            {
                title: '지은/동걸네', 
                latlng: new window.kakao.maps.LatLng(36.10193335258725, 128.419852793029)
            },
            {
                title: '동규네', 
                latlng: new window.kakao.maps.LatLng(36.10295116992656, 128.4197017694798)
            },
        ];

        var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";

        for (var i = 0; i < positions.length; i ++) {
    
            var imageSize = new window.kakao.maps.Size(24, 35);
            
            // var imageSrc = `@/assets/pin${i+1}.png`;
            // console.log(imageSrc);
             
            var markerImage = new window.kakao.maps.MarkerImage(imageSrc, imageSize); 
            
            var marker = new window.kakao.maps.Marker({
                map: map,
                position: positions[i].latlng,
                title : positions[i].title,
                image : markerImage
            });
            console.log(marker);

            var infowindow = new window.kakao.maps.InfoWindow({
                content: positions[i].title
            });

            window.kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
            window.kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        }

        function makeOverListener(map, marker, infowindow) {
            return function() {
                infowindow.open(map, marker);
            };
        }

        function makeOutListener(infowindow) {
            return function() {
                infowindow.close();
            };
        }
    },

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