# TensorFlow Lite C Library for ARMhf (32-bit ARM)

This directory contains the TensorFlow Lite C library compiled for 32-bit ARM (armhf/armv7l) architecture.

## Included File

- `libtensorflowlite_c.so` - TensorFlow Lite C API shared library for armhf (pre-built)

The library is already included and ready to use. The build instructions below are provided for reference in case you need to rebuild the library.

## How to Build (Reference)

### Prerequisites

- ARM cross-compilation toolchain or build on a 32-bit ARM device
- bazelisk
- clang (cross-compiler for ARM if building on x86)

### Option 1: Cross-compile from x86_64

```bash
# Install ARM cross-compilation tools
sudo apt-get install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf

# Clone TensorFlow
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow
git checkout tags/v2.17.1

# Configure for ARMhf cross-compilation
export CC_OPT_FLAGS="-march=armv7-a -mfpu=neon-vfpv4"
export TF_NEED_CUDA=0
export TF_NEED_OPENCL=0
export TF_DOWNLOAD_CLANG=0
export PYTHON_BIN_PATH=$(which python3)

# Build for ARMhf
bazelisk build -c opt \
  --crosstool_top=@org_tensorflow//tools/toolchains/cpus/arm:toolchain \
  --cpu=armeabi-v7a \
  --copt=-march=armv7-a \
  --copt=-mfpu=neon \
  //tensorflow/lite/c:libtensorflowlite_c.so

# Copy the built library to this directory
cp bazel-bin/tensorflow/lite/c/libtensorflowlite_c.so /path/to/linux-voice-assistant/lib/linux_armhf/
```

### Option 2: Build natively on Raspberry Pi or other ARM device

```bash
# On a Raspberry Pi 3/4 (32-bit OS) or similar ARMv7 device
# Install dependencies
sudo apt-get update
sudo apt-get install -y build-essential clang

# Install bazelisk
wget https://github.com/bazelbuild/bazelisk/releases/latest/download/bazelisk-linux-arm -O bazelisk
chmod +x bazelisk
sudo mv bazelisk /usr/local/bin/

# Clone TensorFlow
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow
git checkout tags/v2.17.1

# Build TensorFlow Lite C library
CC=clang bazelisk build -c opt //tensorflow/lite/c:libtensorflowlite_c.so

# Copy the built library
cp bazel-bin/tensorflow/lite/c/libtensorflowlite_c.so /path/to/linux-voice-assistant/lib/linux_armhf/
```

### Option 3: Download pre-built library (if available)

Check the following sources for pre-built armhf binaries:

- TensorFlow official releases (may not include armhf)
- Community builds for Raspberry Pi
- Docker containers with pre-built TensorFlow Lite for ARM

## Verification

After placing the library file, verify it's correct:

```bash
file libtensorflowlite_c.so
# Should show: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV)

ldd libtensorflowlite_c.so
# Check dependencies are available on target system
```

## Notes

- The library should be compiled for ARMv7 with NEON support (armhf) for best compatibility
- Make sure to use TensorFlow version 2.17.1 or compatible version
- Building on native ARM hardware is simpler but may take longer
- Cross-compilation requires proper toolchain setup
