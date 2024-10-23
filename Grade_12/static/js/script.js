
/*
document.addEventListener("DOMContentLoaded", function () {
    console.log("loaded")
    const searchButton = document.getElementById("searchButton")
    const clearButton = document.getElementById("clearButton")
    const searchInput = document.getElementById("searchInput")
    const table = document.getElementById("dataTable")
    const tbody = document.getElementById("tbody")
    const rows = tbody.getElementsByTagName("tr")

    clearButton.addEventListener("click", () => {
        alert("clicked")
    })

    //function to perform search 
    function searchTable() {
        const query = searchInput.value.toLowerCase()
        for (let i = 0; i < rows.length; i++) {
            const nameCell = rows[i].getElementsByTagName("td")[0]
            if (nameCell) {
                const nameText = nameCell.textContent || nameCell.innerText
                if (nameText.toLowerCase().includes(query)) {
                    rows[i].style.display = ""
                } else {
                    rows[i].style.display = "none"
                }

            }
        }

    }

    //function to clear search results
    function clearSearch() {
        searchInput.value = ""
        for (let i = 0; i < rows.length; i++) {
            rows[i].style.display = ""
        }
    }

    //eventListeners
    searchButton.addEventListener("click", searchTable)
    clearButton.addEventListener("click", clearSearch)


})
*/ 

document.addEventListener("DOMContentLoaded", function () {


    const searchButton = document.getElementById("searchButton");
    const clearButton = document.getElementById("clearButton");
    const searchInput = document.getElementById("searchInput");
    const tbody = document.getElementById("tbody"); // Get the correct tbody element
    const rows = tbody.getElementsByTagName("tr");  // Plural function to get all rows

    clearButton.addEventListener("click", () => {   //ALERT
        alert("clicked");
    });

    // Function to perform search
    function searchTable() {
        const query = searchInput.value.toLowerCase();
        for (let i = 0; i < rows.length; i++) {
            const nameCell = rows[i].getElementsByTagName("td")[1];  //SEARCH EDITING 
            if (nameCell) {
                const nameText = nameCell.textContent || nameCell.innerText;
                if (nameText.toLowerCase().includes(query)) {
                    rows[i].style.display = "";
                } else {
                    rows[i].style.display = "none";
                }
            }
        }
    }

    // Function to clear search results
    function clearSearch() {
        searchInput.value = "";
        for (let i = 0; i < rows.length; i++) {
            rows[i].style.display = "";
        }
    }

    // Event listeners
    searchButton.addEventListener("click", searchTable);
    clearButton.addEventListener("click", clearSearch);
});