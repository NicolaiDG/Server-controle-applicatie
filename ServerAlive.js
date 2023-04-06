fetch("url_gelogd.json")
  .then((response) => response.json())
  .then((data) => {
    const url = data.gelogde_lijst_url;
    const ping = data.gelogde_lijst_ping;

    if (url != null) {
      for (i = 0; i < url.length; i++) {
        const li = document.createElement("li");
        const tekst = document.createElement("pre");
        tekst.innerHTML = `URL: ${url[i]}                                                                                                  Ping aangekomen.`;

        li.appendChild(tekst);
        document.getElementById("myList").appendChild(li);

        if (ping[i] === false) {
          const liElements = document.querySelectorAll("li");
          const liElement = liElements.item(i);
          liElement.style.backgroundColor = "red";
          liElement.innerHTML = `URL: ${url[i]} &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Ping niet aangekomen!`;
        }
      }
    }
  });
