#!/bin/bash

#Check for the presence of specific import statement
if ! grep -q 'import React from "react";' main.jsx; then
 echo 'Warning: "import React from "react";" statement not found.'
fi

echo "Main.jsx file checks completed."
