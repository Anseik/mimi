<template>
  <div id="map" class="map-container" style="max-width:800px;height:200px;"></div>
</template>

<script>
export default {
    name: 'CourseMap',
    async mounted() {
        
        const container = document.getElementById('map');
        
        const options = {
            center: new window.kakao.maps.LatLng(36.10253441899348, 128.41969982214542),
            level: 3
        };
        
        const map = new window.kakao.maps.Map(container, options);
        console.log(map);

        const positions = [
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
            {
                title: '싸피', 
                latlng: new window.kakao.maps.LatLng(36.10714973235646, 128.41614601814047)
            },
        ];
        
        const linePath = []
        for (let i = 0; i < positions.length; i ++) {
            linePath.push(positions[i].latlng)
        }

        const polyline = new window.kakao.maps.Polyline({
            path: linePath, // 선을 구성하는 좌표배열
            strokeWeight: 5, // 선의 두께
            strokeColor: '#4A148C', // 선의 색깔
            strokeOpacity: 0.8, // 선의 불투명 - 1에서 0 사이의 값이며 0에 가까울수록 투명
            strokeStyle: 'solid' // 선의 스타일
        });

        polyline.setMap(map); 

        let selectedMarker = null;

        const imageSize = new window.kakao.maps.Size(24, 35);

        for (let i = 0; i < positions.length; i ++) {
    
            let imageSrc = "";
            if (i == 0) {
                imageSrc = "https://i.ibb.co/6RxfQyd/pin1.png";
            } else if (i == 1) {
                imageSrc = "https://i.ibb.co/jy9g2LX/pin2.png";
            } else if (i == 2) {
                imageSrc = "https://i.ibb.co/1MLCC3s/pin3.png";
            } else {
                imageSrc = "https://i.ibb.co/fMMxB05/pin4.png";
            }
            console.log(positions[i])
            addMarker(positions[i], imageSrc)

        }
        
        function addMarker(position, imageSrc) {
            const markerImage = new window.kakao.maps.MarkerImage(imageSrc, imageSize);

            const clickSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
                
            const clickImage = new window.kakao.maps.MarkerImage(clickSrc, imageSize);
            
            
            const marker = new window.kakao.maps.Marker({
                map: map,
                position: position.latlng,
                title : position.title,
                image : markerImage
            });
            marker.markerImage = markerImage;

            window.kakao.maps.event.addListener(marker, 'click', function() {

                if (!selectedMarker || selectedMarker !== marker) {

                    !!selectedMarker && selectedMarker.setImage(selectedMarker.markerImage);

                    marker.setImage(clickImage);
                }

                selectedMarker = marker;
            });

        }
    },

}
</script>

<style>
.map-container {
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
  margin-left: auto;
  margin-right: auto;
}
</style>