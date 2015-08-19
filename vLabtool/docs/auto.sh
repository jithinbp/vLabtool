cp ../experiment.py .
cp -R ../widgets .
cp -R ../templates .

cp ../custom_widgets.py .
cp ../achan.py .
cp ../digital_channel.py .
cp ../interface.py .
cp ../packet_handler.py .
cp ../SPI_class.py .
cp ../I2C_class.py .
cp ../NRF24L01_class.py .
cp ../MCP4728_class.py .
cp ../NRF_NODE.py .
cp ../commands_proto.py .
cp ../customui_rc.py .
cd Apps
rm -r *
cp -R ../../bin/* .
for file in * ; do mv "$file" "${file}.py" ; done
cp ../__appinit__.py ./__init__.py
cd ..

rm -rf docs
sphinx-apidoc -H "vLabtool" -A "Jithin B."  -F -o docs .
cp conf.py docs/conf.py
cp custom.css docs/_static/custom.css
cp index.rst docs/index.rst
cp Apps.rst docs/Apps.rst

cd docs

rm achan.rst
rm commands_proto.rst
rm conf.rst
rm custom_widgets.rst
rm digital_channel.rst
#rm experiment.rst
rm packet_handler.rst
rm template_exp.rst
rm widgets.* templates.* customui_rc
rm MCP4728_class.rst

make html
cp -R ../js _build/html/
