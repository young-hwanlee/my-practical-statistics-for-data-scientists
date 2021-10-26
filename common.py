{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "common.py",
      "provenance": [],
      "authorship_tag": "ABX9TyM4KkEiAa70DflF5B4+WY2M",
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
        "<a href=\"https://colab.research.google.com/github/young-hwanlee/practical-statistics-for-data-scientists/blob/main/common.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Uq41mNoAOp67"
      },
      "source": [
        "from pathlib import Path\n",
        "\n",
        "\n",
        "def dataDirectory(dataDirectoryName='data'):\n",
        "    \"\"\"\n",
        "    Return the directory that contains the data.\n",
        "    \n",
        "    We assume that the data folder is locate in a parent directory of this file and named 'data'.\n",
        "    If your setup is different, you will need to change this method.\n",
        "    \"\"\"\n",
        "    dataDir = Path(__file__).resolve().parent\n",
        "    while not list(dataDir.rglob('data')):\n",
        "        dataDir = dataDir.parent\n",
        "    found = [d for d in dataDir.rglob('data') if d.is_dir()]\n",
        "    if not found:\n",
        "        raise Exception(f'Cannot find data directory with name {dataDirectoryName} along the path of your source files')\n",
        "    return found[0]"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}