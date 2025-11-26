document.getElementById("searchForm").addEventListener("submit", function(event) {
  event.preventDefault();

  const value = document.getElementById("query").value;
  const resultsDiv = document.getElementById("results");

  resultsDiv.innerHTML = '';

  fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(value)}`)
    .then(response => response.json())
    .then(data => {

      console.clear();
      console.log("Search results for:", value);
      console.log(data);

      data.forEach(tvShow => {
        const show = tvShow.show;

        const article = document.createElement("article");

        const h2 = document.createElement("h2");
        h2.textContent = show.name;
        article.appendChild(h2);

        const link = document.createElement("a");
        link.href = show.url;
        link.target = "_blank";
        link.textContent = "Show details";

        article.appendChild(link);

        if (show.image?.medium) {  // Optional chaining
          const img = document.createElement("img");
          img.src = show.image.medium;
          img.alt = show.name;
          article.appendChild(img);
        }

        const summaryDiv = document.createElement("div");
        summaryDiv.innerHTML = show.summary || "No summary available.";
        article.appendChild(summaryDiv);

        resultsDiv.appendChild(article);
      });

    })
    .catch(error => {
      console.error("Error:", error);
    });
});
