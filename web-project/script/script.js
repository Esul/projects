var ALL_CRYPTO = [
  "Bitcoin",
  "Ethereum",
  "Ripple",
  "Litecoin",
  "Dash",
  "NEO",
  "NEM",
  "Monero",
  "IOTA",
  "Qtum",
  "OmiseGO",
  "Zcash",
  "Lisk",
  "Cardano",
  "Tether",
  "EOS",
  "Hshare",
  "Waves",
  "Stratis",
  "Komodo",
  "Ark",
  "Electroneum",
  "Bytecoin",
  "Steem",
  "Ardor",
  "Augur",
  "Populous",
  "Decred",
  "TenX",
  "MaidSafeCoin",
  "BitShares",
  "Golem",
  "PIVX",
  "Gas",
  "TRON",
  "Vertcoin",
  "MonaCoin",
  "Factom",
  "SALT",
  "Dogecoin",
  "DigixDAO",
  "Veritaseum",
  "SingularDTV",
  "Bytom",
  "GameCredits",
  "GXShares",
  "Syscoin",
  "Siacoin",
  "Status",
  "0x",
  "Verge",
  "Lykke",
  "Civic",
  "Blocknet",
  "Metal",
  "Iconomi",
  "Aeternity",
  "DigiByte",
  "Bancor",
  "ATMChain",
  "Gnosis",
  "VeChain",
  "Pura",
  "Particl",
  "FunFair",
  "ChainLink",
  "Nxt",
  "Monaco",
  "Cryptonex",
  "MCAP",
  "Storj",
  "ZenCash",
  "Nexus",
  "Neblio",
  "Zeusshield",
  "ZCoin",
  "AdEx",
  "SmartCash",
  "Loopring",
  "Edgeless",
  "FairCoin",
];
ALL_CRYPTO = ALL_CRYPTO.sort();

// ----------- Starts Tracing of mouse to see if if it's over searchbox

var overSearchBox = false;
var searchBoxList = document.getElementById("searchResults");
searchBoxList.onmouseover = function () {
  overSearchBox = true;
};
searchBoxList.onmouseout = function () {
  overSearchBox = false;
};
//--------------------------------------------------------------------

// ----------- navigation

function home() {
      location.href = "index.html";
}

// ----------- Search

function search() {
  var input, filter, ul, searchBox;
  input = document.getElementById("searchBox");
  filter = input.value.toUpperCase();
  ul = document.getElementById("searchResults");
  while (ul.firstChild) {
    ul.removeChild(ul.firstChild);
  }
  searchBox = document.getElementById("searchBackground");
  searchBox.style.display = "inline-block";

  for (var i = 0; i < ALL_CRYPTO.length; i++) {
    if (ALL_CRYPTO[i].toUpperCase().indexOf(filter) > -1) {
      var entry = document.createElement("li");
      entry.appendChild(document.createTextNode(ALL_CRYPTO[i]));
      ul.appendChild(entry);
    }
  }
  if (filter == "") {
    while (ul.firstChild) {
      ul.removeChild(ul.firstChild);
    }
    hideSearch("backspace");
  }

  findClickedCrypto();
}

function findClickedCrypto() {
  var liList = document
    .getElementById("searchResults")
    .getElementsByTagName("li");

  if (liList.length > 0) {
    for (var i = 0; i < liList.length; i++) {
      liList[i].addEventListener("click", function () {
        goToPage(this.innerHTML);
      });
    }
  }
}

function goToPage(name) {
  // Saving Crypto name to than build it with another JS in new page

  localStorage.setItem("id", name);

  location.href = "cryptoInfo.html";
}

function hideSearch(how) {
  if (how == "backspace")
    document.getElementById("searchBackground").style.display = "none";
  if (how == "blur") {
    if (overSearchBox) {
      return;
    } else {
      document.getElementById("searchBackground").style.display = "none";
    }
  }
}

// --------- fills initial page with prices etc.
async function fill(type) {
  var loaded = false;
  var table = document.getElementById("crTable");
  var rows = table.rows;

  while (true) {
    for (var i = 1; i < rows.length; i++) {
      var cryptoID = getCryptoId(
        rows[i].getElementsByTagName("TD")[1].innerHTML
      ).toLowerCase(); //extract only name without img tag

      var currentPrice = parseFloat(
        rows[i]
          .getElementsByTagName("TD")[2]
          .innerHTML.replace("$", "")
          .replace(/,/g, "")
      );
      var currentMarket = parseFloat(
        rows[i]
          .getElementsByTagName("TD")[3]
          .innerHTML.replace("$", "")
          .replace(/,/g, "")
      );

      // Getting info from API
      var url = `https://api.coingecko.com/api/v3/simple/price?ids=${cryptoID}&vs_currencies=usd&include_market_cap=true`;
      const response = await fetch(url);
      const json = await response.json(); //converting received data to JSON format

      var price = rows[i].getElementsByTagName("TD")[2];
      price.innerHTML =
        "$" +
        json[cryptoID]["usd"].toLocaleString("en-US", {
          maximumFractionDigits: 10,
        });
      var market_cap = rows[i].getElementsByTagName("TD")[3];
      market_cap.innerHTML =
        "$" +
        json[cryptoID]["usd_market_cap"].toLocaleString("en-US", {
          maximumFractionDigits: 2,
        });
      if (loaded) {
        if (currentPrice < parseFloat(json[cryptoID]["usd"].toFixed(10))) {
          price.innerHTML += " ▲";
          price.style.color = "green";
        } else if (
          currentPrice > parseFloat(json[cryptoID]["usd"].toFixed(10))
        ) {
          price.innerHTML += " ▼";
          price.style.color = "red";
        } else {
          price.style.color = "black";
        }

        if (
          currentMarket <
          parseFloat(json[cryptoID]["usd_market_cap"].toFixed(2))
        ) {
          market_cap.innerHTML += " ▲";
          market_cap.style.color = "green";
        } else if (
          currentMarket >
          parseFloat(json[cryptoID]["usd_market_cap"].toFixed(2))
        ) {
          market_cap.innerHTML += " ▼";
          market_cap.style.color = "red";
        } else {
          market_cap.style.color = "black";
        }
      }
      loaded = true;
    }
    await new Promise((r) => setTimeout(r, 4000));
  }
}

function getCryptoId(cryptoID) {
  var i = 0;
  while (cryptoID[i] !== ">") {
    i++;
  }

  return cryptoID.slice(++i).trim();
}

// ------------ Sort Table

function sortTable(n) {
  var table,
    rows,
    switching,
    i,
    x,
    y,
    shouldSwitch,
    dir,
    switchcount = 0;
  table = document.getElementById("crTable");
  switching = true;
  
  dir = "asc";
  
  while (switching) {
  
    switching = false;
    rows = table.rows;
    
    for (i = 1; i < rows.length - 1; i++) {
      
      shouldSwitch = false;
      
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      
      if (n === 1) {  // Vamowmeb tu es sveti aris stringebis (saxelebis sveti) da shesabamisad vadareb mat
        if (dir == "asc") {
          if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        }
      } else { // aq miwevs informaciis gasuftaveba, rom float mnishvnelobebi shevadaro
        if (dir == "asc") {
          if (
            parseFloat(x.innerHTML.replace("$", "").replace(/,/g, "")) >
            parseFloat(y.innerHTML.replace("$", "").replace(/,/g, ""))
          ) {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (
            parseFloat(x.innerHTML.replace("$", "").replace(/,/g, "")) <
            parseFloat(y.innerHTML.replace("$", "").replace(/,/g, ""))
          ) {
            shouldSwitch = true;
            break;
          }
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount++;
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }

  updateAfterSort(n, dir);
}

function updateAfterSort(n, dir) {
  var number, name, price, market;

  number = document.getElementById("tbNumber");
  name = document.getElementById("tbName");
  price = document.getElementById("tbPrice");
  market = document.getElementById("tbMarketCap");

  if (n == 0) {
    if (dir == "asc") {
      number.innerHTML = "# ⬆";
      name.innerHTML = "Name ⬍";
      price.innerHTML = "Price ⬍";
      market.innerHTML = "Market Cap ⬍";
    } else {
      number.innerHTML = "# ⬇";
      name.innerHTML = "Name ⬍";
      price.innerHTML = "Price ⬍";
      market.innerHTML = "Market Cap ⬍";
    }
  }
  if (n == 1) {
    if (dir == "asc") {
      number.innerHTML = "# ⬍";
      name.innerHTML = "Name ⬆";
      price.innerHTML = "Price ⬍";
      market.innerHTML = "Market Cap ⬍";
    } else {
      number.innerHTML = "# ⬍";
      name.innerHTML = "Name ⬇";
      price.innerHTML = "Price ⬍";
      market.innerHTML = "Market Cap ⬍";
    }
  }
  if (n == 2) {
    if (dir == "asc") {
      number.innerHTML = "# ⬍";
      name.innerHTML = "Name ⬍";
      price.innerHTML = "Price ⬆";
      market.innerHTML = "Market Cap ⬍";
    } else {
      number.innerHTML = "# ⬍";
      name.innerHTML = "Name ⬍";
      price.innerHTML = "Price ⬇";
      market.innerHTML = "Market Cap ⬍";
    }
  }
  if (n == 3) {
    if (dir == "asc") {
      number.innerHTML = "# ⬍";
      name.innerHTML = "Name ⬍";
      price.innerHTML = "Price ⬍";
      market = "Market Cap ⬆";
    } else {
      number.innerHTML = "# ⬍";
      name.innerHTML = "Name ⬍";
      price.innerHTML = "Price ⬍";
      market.innerHTML = "Market Cap ⬇";
    }
  }
}
