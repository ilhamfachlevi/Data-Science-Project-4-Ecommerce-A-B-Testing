{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOBIP8p1/cqwIDqSxCPpxF2",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ilhamfachlevi/Data-Science-Project-4-Ecommerce-A-B-Testing/blob/main/ABTesting2022_DS03107_Muhammad_Ilham_Fachlevi_Statistics.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Kaggle Installation"
      ],
      "metadata": {
        "id": "bl5vV5XY3ws-"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "oI5uRAaygy_O"
      },
      "outputs": [],
      "source": [
        "# install kaggle\n",
        "!pip install -q kaggle"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# import kaggle json\n",
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 92
        },
        "id": "TRGthM6J3-nz",
        "outputId": "7a8ab1fd-3205-411f-adf6-1dd60ba5cfa9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-fcbcc09e-90ab-4222-8c19-3fd1aba26e05\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-fcbcc09e-90ab-4222-8c19-3fd1aba26e05\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving kaggle.json to kaggle.json\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'kaggle.json': b'{\"username\":\"milhamfachlevi\",\"key\":\"b7c866182fbd6d70be22a6aff25d66b1\"}'}"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# create a kaggle folder\n",
        "!mkdir ~/.kaggle"
      ],
      "metadata": {
        "id": "ojoiAkqZ4btm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# copy the kaggle.json to folder created  \n",
        "!cp kaggle.json ~/.kaggle/"
      ],
      "metadata": {
        "id": "UJPzpnZX40IS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# permisson for the json to act\n",
        "!chmod 600 ~/.kaggle/kaggle.json"
      ],
      "metadata": {
        "id": "WckfhRJY43yi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# to list all avalaible datasets in kaggle\n",
        "!kaggle datasets list"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bm0mvmwX46Jz",
        "outputId": "77f43412-899b-4e45-8ed4-95f54c331f2b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ref                                                             title                                               size  lastUpdated          downloadCount  voteCount  usabilityRating  \n",
            "--------------------------------------------------------------  ------------------------------------------------  ------  -------------------  -------------  ---------  ---------------  \n",
            "akshaydattatraykhare/diabetes-dataset                           Diabetes Dataset                                     9KB  2022-10-06 08:55:25           6369        210  1.0              \n",
            "whenamancodes/covid-19-coronavirus-pandemic-dataset             COVID -19 Coronavirus Pandemic Dataset              11KB  2022-09-30 04:05:11           5149        164  1.0              \n",
            "akshaydattatraykhare/car-details-dataset                        Car Details Dataset                                 56KB  2022-10-21 06:11:56           1133         29  1.0              \n",
            "whenamancodes/students-performance-in-exams                     Students Performance in Exams                        9KB  2022-09-14 15:14:54           9300        173  1.0              \n",
            "abiodunonadeji/united-state-superstore-sales                    Superstore Sales                                  1002KB  2022-10-08 10:47:57           1574         25  0.7647059        \n",
            "thedevastator/udemy-courses-revenue-generation-and-course-anal  Udemy Courses                                      429KB  2022-10-17 00:11:53            767         33  1.0              \n",
            "vittoriogiatti/bigmacprice                                      Bigmac Prices                                       14KB  2022-10-19 21:11:14           1489         40  1.0              \n",
            "utkarshsaxenadn/vegetable-classifier-acc-9987                   Vegetable Classifier | ResNet50V2 | Acc : 99.87%    89MB  2022-10-21 01:29:02            434         26  1.0              \n",
            "thedevastator/fast-food-restaurants-in-the-united-states        Fast Food Restaurants in the United States           4MB  2022-10-08 17:30:38           1709         46  1.0              \n",
            "whenamancodes/alcohol-effects-on-study                          Alcohol Effects On Study                            18KB  2022-09-15 03:21:04           5728        104  1.0              \n",
            "whenamancodes/student-performance                               Student Performance                                104KB  2022-10-07 05:14:47           5974        137  1.0              \n",
            "narayan63/netflix-popular-movies-dataset                        Netflix popular movies dataset                       1MB  2022-09-24 08:23:22           4138         66  0.9411765        \n",
            "whenamancodes/airbnb-inc-stock-market-analysis                  Airbnb, Inc. Stock Market Analysis                  10KB  2022-10-02 05:44:12            743         32  1.0              \n",
            "eliasturk/world-happiness-based-on-cpi-20152020                 Happiness and Corruption 2015-2020                  29KB  2022-10-11 22:35:03           1120         35  1.0              \n",
            "dansbecker/melbourne-housing-snapshot                           Melbourne Housing Snapshot                         451KB  2018-06-05 12:52:24          98485       1161  0.7058824        \n",
            "arslanali4343/covid19-data-from-world                           COVID-19 data from World                            11MB  2022-10-02 05:56:12           1603         95  0.9411765        \n",
            "whenamancodes/flight-delay-prediction                           Flight Delay Prediction                             31MB  2022-10-07 05:26:20           1776         41  0.88235295       \n",
            "thedevastator/popularity-of-spotify-top-tracks-by-genre         Popularity of Spotify Top Tracks by Genre            9MB  2022-10-18 17:55:53            588         23  0.7647059        \n",
            "anushabellam/cars-cars-2                                        Cars_India_dataset                                   4KB  2022-10-12 06:34:20            981         32  1.0              \n",
            "thedevastator/disney-character-success-a-comprehensive-analysi  Disney Character Success                            39KB  2022-10-08 17:07:22           1052         34  1.0              \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!kaggle datasets download -d putdejudomthai/ecommerce-ab-testing-2022-dataset1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-JT2YBl2482g",
        "outputId": "c10e3109-f783-472a-de19-a03753fab490"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading ecommerce-ab-testing-2022-dataset1.zip to /content\n",
            "\r  0% 0.00/3.29M [00:00<?, ?B/s]\n",
            "\r100% 3.29M/3.29M [00:00<00:00, 85.4MB/s]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qN4Alzi85wYd",
        "outputId": "11966035-4786-4510-8395-27c86476ad5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ecommerce-ab-testing-2022-dataset1.zip  kaggle.json  \u001b[0m\u001b[01;34msample_data\u001b[0m/\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Import Libraries"
      ],
      "metadata": {
        "id": "yO-0M-0d6iKv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import os\n",
        "from sklearn.impute import KNNImputer\n",
        "from scipy.stats import shapiro\n",
        "from scipy.stats import chi2_contingency\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import statsmodels.api as sm\n",
        "import statsmodels.stats.proportion as sp\n",
        "import scipy.stats as stats\n",
        "import zipfile"
      ],
      "metadata": {
        "id": "frKhbdZK6hrx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "with zipfile.ZipFile(\"/content/ecommerce-ab-testing-2022-dataset1.zip\",\"r\") as zip_ref:\n",
        "    zip_ref.extractall(\"ab_testing_2022\")"
      ],
      "metadata": {
        "id": "Zoh5MK3u9jDw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Initializing Variables"
      ],
      "metadata": {
        "id": "IfQLE47NHpMa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ab_data = pd.read_csv('/content/ab_testing_2022/ecommerce_ab_testing_2022_dataset1/ab_data.csv')\n",
        "countries = pd.read_csv('/content/ab_testing_2022/ecommerce_ab_testing_2022_dataset1/countries.csv')"
      ],
      "metadata": {
        "id": "SFEU0vWNE3hL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ab_data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "x3dfa0zkFlnw",
        "outputId": "401eaa9b-6e8e-43fd-e5fb-747b9f67c7ff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        user_id timestamp      group landing_page  converted\n",
              "0        851104   11:48.6    control     old_page          0\n",
              "1        804228   01:45.2    control     old_page          0\n",
              "2        661590   55:06.2  treatment     new_page          0\n",
              "3        853541   28:03.1  treatment     new_page          0\n",
              "4        864975   52:26.2    control     old_page          1\n",
              "...         ...       ...        ...          ...        ...\n",
              "294475   734608   45:03.4    control     old_page          0\n",
              "294476   697314   20:29.0    control     old_page          0\n",
              "294477   715931   40:24.5  treatment     new_page          0\n",
              "294478   759899   20:29.0  treatment     new_page          0\n",
              "294479   643532   40:24.5  treatment     new_page          0\n",
              "\n",
              "[294480 rows x 5 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-782cdec3-df7c-44f6-9582-702a5cbb2054\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>user_id</th>\n",
              "      <th>timestamp</th>\n",
              "      <th>group</th>\n",
              "      <th>landing_page</th>\n",
              "      <th>converted</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>851104</td>\n",
              "      <td>11:48.6</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>804228</td>\n",
              "      <td>01:45.2</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>661590</td>\n",
              "      <td>55:06.2</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>853541</td>\n",
              "      <td>28:03.1</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>864975</td>\n",
              "      <td>52:26.2</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294475</th>\n",
              "      <td>734608</td>\n",
              "      <td>45:03.4</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294476</th>\n",
              "      <td>697314</td>\n",
              "      <td>20:29.0</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294477</th>\n",
              "      <td>715931</td>\n",
              "      <td>40:24.5</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294478</th>\n",
              "      <td>759899</td>\n",
              "      <td>20:29.0</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294479</th>\n",
              "      <td>643532</td>\n",
              "      <td>40:24.5</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>294480 rows ?? 5 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-782cdec3-df7c-44f6-9582-702a5cbb2054')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-782cdec3-df7c-44f6-9582-702a5cbb2054 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-782cdec3-df7c-44f6-9582-702a5cbb2054');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "countries"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "yvT_OT_CGDhM",
        "outputId": "f2d2aed1-5349-4452-9139-fd7d9b777a8c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        user_id country\n",
              "0        834778      UK\n",
              "1        928468      US\n",
              "2        822059      UK\n",
              "3        711597      UK\n",
              "4        710616      UK\n",
              "...         ...     ...\n",
              "290581   799368      UK\n",
              "290582   655535      CA\n",
              "290583   934996      UK\n",
              "290584   759899      US\n",
              "290585   643532      US\n",
              "\n",
              "[290586 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b4cedf60-96f7-4983-8697-554c3df03b77\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>user_id</th>\n",
              "      <th>country</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>834778</td>\n",
              "      <td>UK</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>928468</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>822059</td>\n",
              "      <td>UK</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>711597</td>\n",
              "      <td>UK</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>710616</td>\n",
              "      <td>UK</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>290581</th>\n",
              "      <td>799368</td>\n",
              "      <td>UK</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>290582</th>\n",
              "      <td>655535</td>\n",
              "      <td>CA</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>290583</th>\n",
              "      <td>934996</td>\n",
              "      <td>UK</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>290584</th>\n",
              "      <td>759899</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>290585</th>\n",
              "      <td>643532</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>290586 rows ?? 2 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b4cedf60-96f7-4983-8697-554c3df03b77')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b4cedf60-96f7-4983-8697-554c3df03b77 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b4cedf60-96f7-4983-8697-554c3df03b77');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "countries.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tKcm6jaNI_kd",
        "outputId": "62a98a98-eea4-4802-fc70-414273859ce7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 290586 entries, 0 to 290585\n",
            "Data columns (total 2 columns):\n",
            " #   Column   Non-Null Count   Dtype \n",
            "---  ------   --------------   ----- \n",
            " 0   user_id  290586 non-null  int64 \n",
            " 1   country  290586 non-null  object\n",
            "dtypes: int64(1), object(1)\n",
            "memory usage: 4.4+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Data Cleaning"
      ],
      "metadata": {
        "id": "ubolZy0n4JBZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "countries[countries[\"user_id\"].duplicated()]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 81
        },
        "id": "PbrCHzeNEAY9",
        "outputId": "118e09a2-cf9d-4982-de01-652ae31153fe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        user_id country\n",
              "290584   759899      US"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c8363847-4e0a-4055-9df1-a6544d4e48ef\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>user_id</th>\n",
              "      <th>country</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>290584</th>\n",
              "      <td>759899</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c8363847-4e0a-4055-9df1-a6544d4e48ef')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-c8363847-4e0a-4055-9df1-a6544d4e48ef button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-c8363847-4e0a-4055-9df1-a6544d4e48ef');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "countries[countries[\"user_id\"]==759899]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 112
        },
        "id": "TZznOAYmEF1z",
        "outputId": "42595367-c26b-4b0a-8371-4b7ea86792c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        user_id country\n",
              "105301   759899      US\n",
              "290584   759899      US"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e8a6855b-89db-40a0-bdcd-83dc7984da12\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>user_id</th>\n",
              "      <th>country</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>105301</th>\n",
              "      <td>759899</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>290584</th>\n",
              "      <td>759899</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e8a6855b-89db-40a0-bdcd-83dc7984da12')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e8a6855b-89db-40a0-bdcd-83dc7984da12 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e8a6855b-89db-40a0-bdcd-83dc7984da12');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "countries = countries.drop_duplicates()"
      ],
      "metadata": {
        "id": "o8UALix8Eme9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sum(countries.duplicated())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-WzKw2LnEu4p",
        "outputId": "9711fcb7-69cb-495f-911f-6a3254515c74"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ab_data[ab_data[\"user_id\"].duplicated()]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "JB5hO2hW9emD",
        "outputId": "383399ad-d844-4a3f-d256-8d59f84a92b7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        user_id timestamp      group landing_page  converted\n",
              "2656     698120   13:42.6    control     old_page          0\n",
              "2893     773192   55:59.6  treatment     new_page          0\n",
              "7500     899953   06:54.1    control     new_page          0\n",
              "8036     790934   32:20.3  treatment     new_page          0\n",
              "10218    633793   16:00.7  treatment     old_page          0\n",
              "...         ...       ...        ...          ...        ...\n",
              "294309   787083   15:21.0    control     old_page          0\n",
              "294328   641570   59:27.7    control     old_page          0\n",
              "294331   689637   34:28.3    control     new_page          0\n",
              "294355   744456   32:07.1  treatment     new_page          0\n",
              "294478   759899   20:29.0  treatment     new_page          0\n",
              "\n",
              "[3895 rows x 5 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3a40ffb7-7db9-434c-b683-2710394e89d5\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>user_id</th>\n",
              "      <th>timestamp</th>\n",
              "      <th>group</th>\n",
              "      <th>landing_page</th>\n",
              "      <th>converted</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2656</th>\n",
              "      <td>698120</td>\n",
              "      <td>13:42.6</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2893</th>\n",
              "      <td>773192</td>\n",
              "      <td>55:59.6</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7500</th>\n",
              "      <td>899953</td>\n",
              "      <td>06:54.1</td>\n",
              "      <td>control</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8036</th>\n",
              "      <td>790934</td>\n",
              "      <td>32:20.3</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10218</th>\n",
              "      <td>633793</td>\n",
              "      <td>16:00.7</td>\n",
              "      <td>treatment</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294309</th>\n",
              "      <td>787083</td>\n",
              "      <td>15:21.0</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294328</th>\n",
              "      <td>641570</td>\n",
              "      <td>59:27.7</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294331</th>\n",
              "      <td>689637</td>\n",
              "      <td>34:28.3</td>\n",
              "      <td>control</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294355</th>\n",
              "      <td>744456</td>\n",
              "      <td>32:07.1</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294478</th>\n",
              "      <td>759899</td>\n",
              "      <td>20:29.0</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>3895 rows ?? 5 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3a40ffb7-7db9-434c-b683-2710394e89d5')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3a40ffb7-7db9-434c-b683-2710394e89d5 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3a40ffb7-7db9-434c-b683-2710394e89d5');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ab_data = ab_data.drop_duplicates()"
      ],
      "metadata": {
        "id": "quKw7ndz9Z4A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sum(ab_data.duplicated())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m9V162rb9xNR",
        "outputId": "63b54b1a-8665-413d-9017-e2b8ef471e3f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Merging Data"
      ],
      "metadata": {
        "id": "qxe4rLQsKUFk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df = ab_data.merge(countries)\n",
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "lvcoriUIJY6M",
        "outputId": "e784201b-7d04-427d-e925-bbc996dbd87f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        user_id timestamp      group landing_page  converted country\n",
              "0        851104   11:48.6    control     old_page          0      US\n",
              "1        804228   01:45.2    control     old_page          0      US\n",
              "2        661590   55:06.2  treatment     new_page          0      US\n",
              "3        853541   28:03.1  treatment     new_page          0      US\n",
              "4        864975   52:26.2    control     old_page          1      US\n",
              "...         ...       ...        ...          ...        ...     ...\n",
              "294475   945152   51:57.1    control     old_page          0      US\n",
              "294476   734608   45:03.4    control     old_page          0      US\n",
              "294477   697314   20:29.0    control     old_page          0      US\n",
              "294478   715931   40:24.5  treatment     new_page          0      UK\n",
              "294479   643532   40:24.5  treatment     new_page          0      US\n",
              "\n",
              "[294480 rows x 6 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-bce62b72-77f6-4b02-875b-d1e152c9a0ab\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>user_id</th>\n",
              "      <th>timestamp</th>\n",
              "      <th>group</th>\n",
              "      <th>landing_page</th>\n",
              "      <th>converted</th>\n",
              "      <th>country</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>851104</td>\n",
              "      <td>11:48.6</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>804228</td>\n",
              "      <td>01:45.2</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>661590</td>\n",
              "      <td>55:06.2</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>853541</td>\n",
              "      <td>28:03.1</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>864975</td>\n",
              "      <td>52:26.2</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>1</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294475</th>\n",
              "      <td>945152</td>\n",
              "      <td>51:57.1</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294476</th>\n",
              "      <td>734608</td>\n",
              "      <td>45:03.4</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294477</th>\n",
              "      <td>697314</td>\n",
              "      <td>20:29.0</td>\n",
              "      <td>control</td>\n",
              "      <td>old_page</td>\n",
              "      <td>0</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294478</th>\n",
              "      <td>715931</td>\n",
              "      <td>40:24.5</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "      <td>UK</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>294479</th>\n",
              "      <td>643532</td>\n",
              "      <td>40:24.5</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>294480 rows ?? 6 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-bce62b72-77f6-4b02-875b-d1e152c9a0ab')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-bce62b72-77f6-4b02-875b-d1e152c9a0ab button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-bce62b72-77f6-4b02-875b-d1e152c9a0ab');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.sample()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 81
        },
        "id": "MgSoJgZD-K1C",
        "outputId": "ced4dd86-beae-4b58-8e00-a3511f8d5142"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        user_id timestamp      group landing_page  converted country\n",
              "149806   697869   26:35.6  treatment     new_page          0      US"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-302ab52b-350d-4525-ab51-52bdb6115d0d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>user_id</th>\n",
              "      <th>timestamp</th>\n",
              "      <th>group</th>\n",
              "      <th>landing_page</th>\n",
              "      <th>converted</th>\n",
              "      <th>country</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>149806</th>\n",
              "      <td>697869</td>\n",
              "      <td>26:35.6</td>\n",
              "      <td>treatment</td>\n",
              "      <td>new_page</td>\n",
              "      <td>0</td>\n",
              "      <td>US</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-302ab52b-350d-4525-ab51-52bdb6115d0d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-302ab52b-350d-4525-ab51-52bdb6115d0d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-302ab52b-350d-4525-ab51-52bdb6115d0d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Iq82JTONcIc8",
        "outputId": "43d79ca1-46c1-485b-a00e-33b49a101ec7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 294480 entries, 0 to 294479\n",
            "Data columns (total 6 columns):\n",
            " #   Column        Non-Null Count   Dtype \n",
            "---  ------        --------------   ----- \n",
            " 0   user_id       294480 non-null  int64 \n",
            " 1   timestamp     294480 non-null  object\n",
            " 2   group         294480 non-null  object\n",
            " 3   landing_page  294480 non-null  object\n",
            " 4   converted     294480 non-null  int64 \n",
            " 5   country       294480 non-null  object\n",
            "dtypes: int64(2), object(4)\n",
            "memory usage: 15.7+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[['group','landing_page']] = df[['group','landing_page']].astype('category')\n",
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_Y4yAKhh1bcC",
        "outputId": "1a4a69a3-985a-4d7b-8c89-cdee32ec5b8a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 294480 entries, 0 to 294479\n",
            "Data columns (total 6 columns):\n",
            " #   Column        Non-Null Count   Dtype   \n",
            "---  ------        --------------   -----   \n",
            " 0   user_id       294480 non-null  int64   \n",
            " 1   timestamp     294480 non-null  object  \n",
            " 2   group         294480 non-null  category\n",
            " 3   landing_page  294480 non-null  category\n",
            " 4   converted     294480 non-null  int64   \n",
            " 5   country       294480 non-null  object  \n",
            "dtypes: category(2), int64(2), object(2)\n",
            "memory usage: 11.8+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Defining Set & Searching for Mismatch from Dataset"
      ],
      "metadata": {
        "id": "WSYhtfu9Rdva"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "set(list(df['landing_page']))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QWgycCfRRkpz",
        "outputId": "77c3ac81-cc27-4209-95ab-fdd4040acebe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'new_page', 'old_page'}"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "set(list(df['group']))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6j6mjhTz1D9H",
        "outputId": "892cbeb1-45ce-40b5-bd1d-47f95c9e7b92"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'control', 'treatment'}"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mismatch = df[(df[\"group\"]==\"control\")&(df[\"landing_page\"]==\"new_page\")\n",
        "                |(df[\"group\"]==\"treatment\")&(df[\"landing_page\"]==\"old_page\")].index\n",
        "number_mismatch = mismatch.shape[0]\n",
        "print(f\"Number of Mismatch:{number_mismatch} rows\" )\n",
        "print(\"Mismatch Percentage:%.1f%%\" % (number_mismatch/df.shape[0]*100), \"rows\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "scmmZUzWBS3C",
        "outputId": "03a5bcb6-606f-4048-ed20-f257de248058"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of Mismatch:3893 rows\n",
            "Mismatch Percentage:1.3% rows\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.drop(mismatch, inplace = True)"
      ],
      "metadata": {
        "id": "LnV1N4mZC1d-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.drop_duplicates(subset=\"user_id\", inplace = True)"
      ],
      "metadata": {
        "id": "s_QtSiaGDJWK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rT9Le3GHDMHO",
        "outputId": "70dc2f64-6e39-4e0d-bd9e-4e80b73b370a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 290585 entries, 0 to 294479\n",
            "Data columns (total 6 columns):\n",
            " #   Column        Non-Null Count   Dtype   \n",
            "---  ------        --------------   -----   \n",
            " 0   user_id       290585 non-null  int64   \n",
            " 1   timestamp     290585 non-null  object  \n",
            " 2   group         290585 non-null  category\n",
            " 3   landing_page  290585 non-null  category\n",
            " 4   converted     290585 non-null  int64   \n",
            " 5   country       290585 non-null  object  \n",
            "dtypes: category(2), int64(2), object(2)\n",
            "memory usage: 11.6+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3BjyANntDr9f",
        "outputId": "ab935a85-80d5-4ba7-9e82-7ea7e6ec051d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(290585, 6)"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[df[\"user_id\"].duplicated()]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 49
        },
        "id": "UpnK6DsEE7vR",
        "outputId": "455d650f-4a06-43d0-c2ea-d6d017bd04fe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Empty DataFrame\n",
              "Columns: [user_id, timestamp, group, landing_page, converted, country]\n",
              "Index: []"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3d19f3c2-7125-4bdb-a77e-08dfa93fc8d6\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>user_id</th>\n",
              "      <th>timestamp</th>\n",
              "      <th>group</th>\n",
              "      <th>landing_page</th>\n",
              "      <th>converted</th>\n",
              "      <th>country</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3d19f3c2-7125-4bdb-a77e-08dfa93fc8d6')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3d19f3c2-7125-4bdb-a77e-08dfa93fc8d6 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3d19f3c2-7125-4bdb-a77e-08dfa93fc8d6');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Data Visualization EDA"
      ],
      "metadata": {
        "id": "i4uOspZrMhf4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df['group'].value_counts().plot.pie(autopct='%1.1f%%', shadow=True)\n",
        "\n",
        "plt.title(f\"Persentase Customers in Each Group\", weight='bold')\n",
        "plt.legend()    \n",
        "plt.show()"
      ],
      "metadata": {
        "id": "0Z4GcVIOSiNi",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 264
        },
        "outputId": "e754abbd-da21-4bef-9eed-8c3a2841dc3d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "myexplode = [0, 0.2]\n",
        "df['converted'].value_counts(ascending=False).plot.pie(autopct='%1.1f%%', shadow=True, explode=myexplode)\n",
        "\n",
        "plt.title(f\"Persentase Customers based on Converted\", weight='bold')\n",
        "plt.legend()    \n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 264
        },
        "id": "waoZ-PQkG0tT",
        "outputId": "d18ea31a-ec35-4b39-a2ed-08da40c5072a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['landing_page'].value_counts().plot.pie(autopct='%1.1f%%', shadow=True)\n",
        "\n",
        "plt.title(f\"Percentage of Treatment to Customers\", weight='bold')\n",
        "plt.legend()\n",
        "    \n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 264
        },
        "id": "gctzbSWsJGnZ",
        "outputId": "6024331e-8875-4b49-b70b-be3cd7feb236"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig = plt.figure(figsize=(10,5))\n",
        "sns.countplot(data=df,x=\"group\", hue=\"country\", palette='deep')\n",
        "\n",
        "plt.title(f\"US vs CA vs UK\", weight='bold')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 350
        },
        "id": "QfKdAnv4IMnk",
        "outputId": "60f7adaf-4d28-42e3-fbc7-550f852cad3f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x360 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig = plt.figure(figsize=(10,5))\n",
        "sns.countplot(data=df,x=\"landing_page\", hue=\"country\", palette='deep')\n",
        "\n",
        "plt.title(f\"US vs CA vs UK\", weight='bold')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 352
        },
        "id": "g-ljzLMOIxVS",
        "outputId": "aa3e19f6-9054-44f7-b8bb-c424e662fda6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x360 with 1 Axes>"
            ],
            "image/png": "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6AHA7bffzn777ceRRx7JjjvuyLHHHktmcvHFF/Pss8+y//77s//++y/f50tf+hKDBg3i3HPP5fDDD1/e3+TJkxkxYkSH/jbvlpUkSeuVmTNncs455/D73/+enj17smDBAkaNGrX8M27cOE4//XR+8YtftNnP/fffz8yZM+nTpw/77LMPd911F6effjrf+c53mDp1Kj179gTg73//O3vttRcXXHABmclOO+3EvHnz6NWrF+PHj+fTn/50h/4+w12TfPIrVzV7COuEn3372GYPQZJUMVOmTOGoo45aHr623HJL7r77bq677joAjjvuOL7yla+stJ8999yTvn37ArDbbrsxe/Zshg4d+rZ2Xbp04YgjjgBqN0gcd9xx/PSnP2X06NHcfffdTJgwoaN+GtDAcBcR44CPAnMzc5dS2xL4OdAPmA0cnZkLo3YryEXAIcA/gBMy876yzyjg30q352TmFaU+GLgc2Bi4CfhCZmZrx2jU75SktYl/OLaPfziqvbp27cobb7wBwBtvvMHSpUuXb9too42WL3fp0oXXXnutxT66d+9Oly5dlq+PHj2aQw89lO7du3PUUUfRtWvHxrFGXnN3OTB8hdpXgdsyc3vgtrIOcDCwffmMAX4Iy8PgWcBewJ7AWRGxRdnnh8BJdfsNX8kxJEmSGDZsGNdccw3z588HYMGCBXzwgx9k0qRJAFx11VXsu+++APTr148ZM2YAcOONN/Lqq6+utP/NNtuMl19+udXtffr0oU+fPpxzzjmMHj16TX/O2zQs3GXmHcCCFcqHAVeU5SuAw+vqE7JmGrB5RPQGDgImZ+aCMvs2GRhetr0jM6dlZgITVuirpWNIkiSx88478/Wvf50Pf/jDDBo0iDPPPJPvfe97jB8/nl133ZUrr7ySiy66CICTTjqJ3/72twwaNIi7776bTTfddKX9jxkzhuHDhy+/oaIlxx57LNtuuy077bRTh/2uZTr7mrutM/O5svw8sHVZ3gZ4uq7dnFJrqz6nhXpbx5AkSQJYfvNEvSlTpryt3dZbb820adOWr5933nkA7Lfffuy3337L65dccsny5dNOO43TTjtt+frixYvf1u+dd97JSSedtNrjb0vTbqgo18dlM48REWOonQZmu+22a+RQJEmSABg8eDCbbropF1xwQUP67+zn3L1QTqlSvueW+jPAtnXt+pZaW/W+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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Conversion Rate"
      ],
      "metadata": {
        "id": "FV1SQ9VlLPVJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "control = df[df[\"group\"] == \"control\"]\n",
        "treatment = df[df[\"group\"] == \"treatment\"]\n",
        "\n",
        "control_perc = round(control.converted.sum() / control.converted.shape[0] * 100, 2)\n",
        "treatment_perc = round(treatment.converted.sum() / treatment.converted.shape[0] * 100, 2)\n",
        "\n",
        "print(f\"Control Conversion Rate: {control_perc}%\")\n",
        "print(f\"Treatment Conversion Rate: {treatment_perc}%\")"
      ],
      "metadata": {
        "id": "OgeaBItdSkFh",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "717ebbc7-8d4b-49f5-e792-f1929f463546"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Control Conversion Rate: 12.04%\n",
            "Treatment Conversion Rate: 11.88%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "total_spend = df.groupby(['landing_page'])['converted'].sum().reset_index()\n",
        "total_spend"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 112
        },
        "id": "NCvR7IEEMn8T",
        "outputId": "f1816199-5c77-4ae4-a935-09bccb49d83b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  landing_page  converted\n",
              "0     new_page      17264\n",
              "1     old_page      17489"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a60a4441-5408-46f1-b256-2fce488ea2e3\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>landing_page</th>\n",
              "      <th>converted</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>new_page</td>\n",
              "      <td>17264</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>old_page</td>\n",
              "      <td>17489</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a60a4441-5408-46f1-b256-2fce488ea2e3')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a60a4441-5408-46f1-b256-2fce488ea2e3 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a60a4441-5408-46f1-b256-2fce488ea2e3');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Checking Data Distribution"
      ],
      "metadata": {
        "id": "RZXT2cmtPG-7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "groupA = df[df['landing_page'] == \"old_page\"]['converted']\n",
        "groupB = df[df['landing_page'] == \"new_page\"]['converted']"
      ],
      "metadata": {
        "id": "klAvLltxOE5r"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ntA = shapiro(groupA)[1] < 0.05\n",
        "ntB = shapiro(groupB)[1] < 0.05"
      ],
      "metadata": {
        "id": "KDNB0XyMOQtA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(ntA,ntB)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aSb_k9_KOr9F",
        "outputId": "15d8a0de-81f3-47eb-8d8d-ccbf4188bc90"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        " leveneTest = stats.levene(groupA, groupB)[1] < 0.05"
      ],
      "metadata": {
        "id": "GZCnKnb5RNon"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "leveneTest"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U3VmFZWTR9ZJ",
        "outputId": "85b62e88-b3a2-4a82-aeb2-f17019aeaf67"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Chi Squared Test & P value Test"
      ],
      "metadata": {
        "id": "_LYSKKCWN5Hw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "control_converted = control[\"converted\"].sum()\n",
        "treatment_converted = treatment[\"converted\"].sum()\n",
        "control_not_converted = control[\"converted\"].count() - control_converted\n",
        "treatment_not_converted = treatment[\"converted\"].count() - treatment_converted\n",
        "contignency_table = np.array([[control_converted, control_not_converted],\n",
        "                             [treatment_converted, treatment_not_converted]])"
      ],
      "metadata": {
        "id": "8w_NqohoOs7f"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "chi, p_value, _, _ = chi2_contingency(contignency_table, correction=False)"
      ],
      "metadata": {
        "id": "JoIU0WKwO5KY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "chi, p_value"
      ],
      "metadata": {
        "id": "j25elqX8PDxH",
        "outputId": "13411019-3036-4418-a87c-35ac8dd24742",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1.720314323018192, 0.1896525897188101)"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ttest = stats.ttest_ind(groupA, groupB, equal_var=True)[1]"
      ],
      "metadata": {
        "id": "-lTnGx-OSRz5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ttest"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vZxAhyK2STYp",
        "outputId": "c68ea214-376c-469b-8928-4fd6feb7d065"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.18965383906859376"
            ]
          },
          "metadata": {},
          "execution_count": 64
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ttest = stats.mannwhitneyu(groupA, groupB)[1] "
      ],
      "metadata": {
        "id": "DtmAiv7WTT8E"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ttest"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "si41uSXdTVIq",
        "outputId": "8377809d-6951-443e-f45f-4fb242d655c6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.18965336487086848"
            ]
          },
          "metadata": {},
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "alpha = round(1 - 0.95, 2)\n",
        "print(f\"Significance: {alpha}, p-value: {p_value}\")\n",
        "\n",
        "if p_value <= alpha:\n",
        "    print(\"Success to reject H0 \")\n",
        "else:\n",
        "    print(\"Failed to reject H0\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HeUgom6BQaL7",
        "outputId": "74c7a23c-1bcb-404d-81bd-5dd4724a6f5c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Significance: 0.05, p-value: 0.1896525897188101\n",
            "Failed to reject H0\n"
          ]
        }
      ]
    }
  ]
}