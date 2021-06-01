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

async function build() {
  var cryptoName = localStorage.getItem("id").toLowerCase();

  var URL = `https://api.coingecko.com/api/v3/coins/${cryptoName}`;

  // Getting info from API
  const response = await fetch(URL);
  const json = await response.json(); //converting received data to JSON format

  // Building the page
  var description = document.getElementById("cryptoDescription");
  var title = document.getElementById("headerCrypto");
  var img = document.getElementById("cryptoThumb");
  var price = document.getElementById("currentPrice");
  var dayChange = document.getElementById("dayChange");
  var weekChange = document.getElementById("weekChange");
  var perc24 = json["market_data"]["price_change_percentage_24h"];
  var percWeek = json["market_data"]["price_change_percentage_7d"];

  img.src = json["image"]["large"];

  title.innerHTML +=
    json["name"] +
    " - $" +
    json["market_data"]["current_price"]["usd"].toLocaleString("en-US", {
      maximumFractionDigits: 10,
    }) +
    " ";
  for (var j = 0; j < 2; j++) addChart(cryptoName, j);

  if (perc24 > 0) {
    dayChange.innerHTML += "▲ " + perc24 + " %";
    dayChange.style.color = "green";
  } else {
    dayChange.innerHTML += "▼ " + perc24 + " %";
    dayChange.style.color = "red";
  }

  if (percWeek > 0) {
    weekChange.innerHTML += "▲ " + percWeek + " %";
    weekChange.style.color = "green";
  } else {
    weekChange.innerHTML += "▼ " + percWeek + " %";
    weekChange.style.color = "red";
  }

  description.innerHTML =
    "<h3 style='display: inline'>Brief Description: </h3> " +
    json["description"]["en"];
}

async function addChart(cryptoName, j) {
  if (j === 0)
    var URL = `https://api.coingecko.com/api/v3/coins/${cryptoName}/market_chart?vs_currency=usd&days=1&interval=hourly`;
  else
    var URL = `https://api.coingecko.com/api/v3/coins/${cryptoName}/market_chart?vs_currency=usd&days=7&interval=hourly`;
  const response = await fetch(URL);
  const json = await response.json(); //converting received data to JSON format

  var xy = [];
  xy = json["prices"];

  for (var i = 0; i < json["prices"].length; i++) {
    xy[i][0] = new Date(xy[i][0]);
  }

  google.charts.load("current", { packages: ["corechart", "line"] });
  google.charts.setOnLoadCallback(drawCurveTypes);

  function drawCurveTypes() {
    var data = new google.visualization.DataTable();
    if (j === 0) data.addColumn("date", "24 hour");
    else data.addColumn("date", "7 days");

    data.addColumn("number", cryptoName);

    data.addRows(xy);

    var options = {
      legend: "none",
      colors: ["blue"],
      backgroundColor: "#eeeeee",
      hAxis: {
        title: "Time",
      },
      vAxis: {
        title: "Price $",
      },
      series: {
        1: { curveType: "function" },
      },
    };

    // Cheking if price has risen since beggining and giving correspongind color
    if (xy[0][1] < xy[xy.length - 1][1]) options["colors"][0] = "green";
    else if (xy[0][1] > xy[xy.length - 1][1]) options["colors"][0] = "red";
    else {
      //pass
    }

    // Checking if 24 or 7 day chart and giving appropriate label
    if (j === 0) options["hAxis"]["title"] = "24 hours";
    else options["hAxis"]["title"] = "7 days";

    var chart = new google.visualization.LineChart(
      document.getElementById(`chart_div${j}`)
    );
    chart.draw(data, options);
  }
}
