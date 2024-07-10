#!/bin/bash
# This is a Linux shell script to download a model from Hugging Face

# Enable Hugging Face transfer
echo "Enabling Hugging Face transfer..."
export HF_HUB_ENABLE_HF_TRANSFER=1

# Start downloading the model
echo "Starting download of the model EleutherAI/gpt-j-6b..."
huggingface-cli download EleutherAI/gpt-j-6b

# Check if the download was successful
if [ $? -ne 0 ]; then
    echo "Download failed!"
else
    echo "Download completed successfully!"
fi

# Pause to keep the window open (for terminal)
read -p "Press any key to continue..."