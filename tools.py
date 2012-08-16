from __future__ import division, print_function, unicode_literals

from xml.dom.minidom import Document


def generate_img_xml():
    '''
    <?xml version='1.0' ?>
    <wml>
      <card id='main'>
        <p>
          This is a test!
        </p>
      </card>
    </wml>
    
    <resource>
     <imageatlas size='128x128' file='road-tiles.png'>
        <image id='i-tl' offset='0,384' />
    '''
    
    #SET MANUALLY:
    w = 1920  
    h = 1080
    
    ###############
    # Create the minidom document
    doc = Document()
    
    res = doc.createElement('resource')
    doc.appendChild(res)
    
    imga = doc.createElement('imageatlas')
    imga.setAttribute('size', '128x128')
    imga.setAttribute('file', 'test.png')
    res.appendChild(imga)
    
    tileset = doc.createElement('tileset')
    res.appendChild(tileset)
    
    ##################
    # Create the minidom document
    map = Document()
    
    base = map.createElement('resource')
    map.appendChild(base)
    req = map.createElement('requires')
    req.setAttribute('file','test_tile.xml')
    base.appendChild(req)
    
    rectmap = map.createElement('rectmap')
    rectmap.setAttribute('id','testmap')
    rectmap.setAttribute('origin','0,0,0')
    rectmap.setAttribute('tile_size','128x128')
    
    
    # Create a image element
    count=0
    for x in xrange(0,w,128):
        col = map.createElement('column')
        for y in xrange(0,w,128):
            count+=1
            img = doc.createElement('image')
            img.setAttribute('id', '%d'%count)
            img.setAttribute('offset', '%d,%d'%(x,y))
            imga.appendChild(img)
            
            tile = doc.createElement('tile')
            tile.setAttribute('id', 't-%d'%count)
            imgref = doc.createElement('image')
            imgref.setAttribute('ref', '%d' % count )
            tile.appendChild(imgref)
            tileset.appendChild(tile)
            
            ###
            
            cell = map.createElement('cell')
            cell.setAttribute( 'tile' , 't-%d' % count )
            col.appendChild( cell )
        
        rectmap.appendChild(col)
    
    base.appendChild(rectmap)
    
    with open("test_tile.xml", "w") as f:
        f.write(doc.toprettyxml(indent="  "))
        
    with open("test_map.xml", "w") as f:
        f.write(map.toprettyxml(indent="  "))
        
def generate_testcard():
    '''
    <?xml version='1.0' ?>
    <wml>
      <card id='main'>
        <p>
          This is a test!
        </p>
      </card>
    </wml>
    
    <resource>
     <imageatlas size='128x128' file='road-tiles.png'>
        <image id='i-tl' offset='0,384' />
    '''
    
    #SET MANUALLY:
    w = 1920  
    h = 1080
    
    ##################
    # Create the minidom document
    map = Document()
    
    base = map.createElement('resource')
    map.appendChild(base)

    
    rectmap = map.createElement('rectmap')
    rectmap.setAttribute('id','testmap')
    rectmap.setAttribute('origin','0,0,0')
    rectmap.setAttribute('tile_size','128x128')
    
    
    # Create a image element
    count=0
    for x in xrange(0,w,128):
        col = map.createElement('column')
        for y in xrange(0,w,128):
            
            cell = map.createElement('cell')
            cell.setAttribute( 'tile' , 'img_tile' )
            col.appendChild( cell )
        
        rectmap.appendChild(col)
    
    base.appendChild(rectmap)
    
    with open("test_card.xml", "w") as f:
        f.write(map.toprettyxml(indent="  "))
