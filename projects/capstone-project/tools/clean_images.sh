# Clean images from Train, Validation and Test folders

echo "Removing parasitized train images"
rm ../data/train/parasitized/*.png
echo "Removing parasitized validation images"
rm ../data/validation/parasitized/*.png
echo "Removing parasitized test images"
rm ../data/test/parasitized/*.png

echo "Removing uninfected train images"
rm ../data/train/uninfected/*.png
echo "Removing uninfected validation images"
rm ../data/validation/uninfected/*.png
echo "Removing uninfected test images"
rm ../data/test/uninfected/*.png

echo "Removing preview images"
rm ../data/preview/*.png