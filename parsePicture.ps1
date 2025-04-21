Add-Type -AssemblyName System.Drawing
$imagePath = "C:\\\\repo\\funksi\\picross\\test.png"
$bitmap = New-Object System.Drawing.Bitmap($imagePath)

$width = $bitmap.Width
$height = $bitmap.Height
$pixels = '';
for ($y = 0; $y -lt $height; $y++) {
    for ($x = 0; $x -lt $width; $x++) {
        $pixelColor = $bitmap.GetPixel($x, $y)
        
        # Access color components
        $alpha = $pixelColor.A
        $red = $pixelColor.R
        $green = $pixelColor.G
        $blue = $pixelColor.B

        # Process pixel data (example: print RGB values)
        Write-Host "Pixel at ($x,$y): Alpha=$alpha, Red=$red, Green=$green, Blue=$blue"
		$pixels += ";$red,$green,$blue"
    }
}
$pixels += ";"
$pixels = $pixels.Substring(1)
$bitmap.Dispose()
Write-Host "---------------" 
Write-Host "$pixels" 
Write-Host "---------------" 