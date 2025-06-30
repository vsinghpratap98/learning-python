{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNRdlIPavsfTkn390qNSuB3",
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
        "<a href=\"https://colab.research.google.com/github/deepaksingh4190/learning-python/blob/main/BMI_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "ZeVQG7vM0kiK",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8e6ee3e8-fcb5-4d6e-a700-b8e2fb661818"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the height (m): 2\n",
            "Enter your height (kg): 45\n",
            "Your status is 'underweight'\n",
            "your bmi is 11.2\n"
          ]
        }
      ],
      "source": [
        "# BMI calculator\n",
        "\n",
        "Height = float(input(\"Enter the height (m): \"))\n",
        "Weight = float(input(\"Enter your height (kg): \"))\n",
        "\n",
        "# calculating BMI\n",
        "\n",
        "BMI = Weight / (Height * Height)\n",
        "\n",
        "if BMI < 18.5:\n",
        "  print(\"Your status is 'underweight'\") #for less than 18.5\n",
        "\n",
        "elif BMI < 25:\n",
        "  print(\"Ok you 'normal'\") #for less than 25\n",
        "\n",
        "elif BMI < 30:\n",
        "  print(\"Its 'overweight'\") #for less than 30\n",
        "\n",
        "else:\n",
        "  print(\"You are suffering from 'obesity'\") # if greater than 30 it will be obesity\n",
        "\n",
        "print(f\"your bmi is {BMI:.1f}\") #formatting bmi for decimal\n"
      ]
    }
  ]
}