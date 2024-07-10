@echo off
:: This is a Windows batch script to download a model from Hugging Face

:: Enable Hugging Face transfer
echo Enabling Hugging Face transfer...
set HF_HUB_ENABLE_HF_TRANSFER=1

:: Start downloading the model
echo Starting download of the model EleutherAI/gpt-j-6b...
huggingface-cli download EleutherAI/gpt-j-6b

:: Check if the download was successful
if %errorlevel% neq 0 (
    echo Download failed!
) else (
    echo Download completed successfully!
)

:: Pause to keep the window open
pause