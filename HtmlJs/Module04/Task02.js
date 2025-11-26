document.getElementById("searchForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Stop normal form submission

  const value = document.getElementById("query").value;


  fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(value)}`)
    .then(response => response.json())
    .then(data => {
      console.clear();
      console.log("Search results for:", value);
      console.log(data);
    })
    .catch(error => {
      console.error("Error:", error);
    });
});
