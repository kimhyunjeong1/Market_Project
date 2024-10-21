// 카메라 아이콘을 클릭하면 파일 선택 창을 엽니다.
document.getElementById('cameraIcon').addEventListener('click', function() {
    document.getElementById('fileInput').click(); // input 요소 클릭
  });
  
  // 파일이 선택되었을 때 미리보기 이미지를 업데이트합니다.
  document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0]; // 선택된 파일 가져오기
    if (file) {
      const reader = new FileReader(); // FileReader 객체 생성
      reader.onload = function(e) {
        document.getElementById('cameraIcon').src = e.target.result; // 이미지 미리보기
      };
      reader.readAsDataURL(file); // 선택된 파일을 데이터 URL로 읽어오기
    }
  });
  