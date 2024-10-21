// 검색 버튼 클릭 이벤트
document.getElementById("searchButton").addEventListener("click", function () {
  const searchValue = document.getElementById("searchInput").value;
  if (searchValue) {
    // 검색어 출력 (여기서 실제 검색 로직을 구현 가능)
    console.log("검색어:", searchValue);
  } else {
    alert("검색어를 입력하세요.");
  }
});

// 엔터 키 입력 시 검색
document
  .getElementById("searchInput")
  .addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      const searchValue = e.target.value;
      if (searchValue) {
        // 검색어 출력 (여기서 실제 검색 로직을 구현 가능)
        console.log("검색어:", searchValue);
      } else {
        alert("검색어를 입력하세요.");
      }
    }
  });
