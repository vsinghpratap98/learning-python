{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOmozY34rMEwkpOkVg3yx3O",
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
        "<a href=\"https://colab.research.google.com/github/deepaksingh4190/learning-python/blob/main/p1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k2dqUhBOsLrT",
        "outputId": "3b863758-8ce6-420e-c278-e3670535c9de"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello World\n"
          ]
        }
      ],
      "source": [
        "print(\"hello World\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "rows= 5\n",
        "for i in range (1,rows+1):\n",
        "  for space in range(rows-i):\n",
        "    print(\" \",end=\" \")\n",
        "  for star in range(i):\n",
        "    print(\"*\",end=\" \")\n",
        "  print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eneeWkoSuUjC",
        "outputId": "32d23388-650e-424d-82b1-c54c2a777fc0"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "        * \n",
            "      * * \n",
            "    * * * \n",
            "  * * * * \n",
            "* * * * * \n"
          ]
        }
      ]
    }
  ]
}