package tsmapper;
import java.awt.*;
import java.awt.event.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;
import javafx.scene.input.KeyCode;
import javax.swing.*;
import javax.swing.border.AbstractBorder;
import javax.swing.border.Border;

public class TSMapper
{
    public static void
    main( String[] args )
    {
        TSMapperClass object = new TSMapperClass();
    }
}

class TSMapperClass implements KeyListener
{
    final String[] DIRECT = { "North", "East", "South", "West" };
    final int WIDTH, HEIGHT, LEVELS, OFFSET_X, OFFSET_Y, OFFSET_L; // ARRAY OFFSETS ( array needs positive values )
    final Color LIGHT_GRAY, DARK_GRAY;
    boolean[][][][] m_grid;
    JPanel m_gridGUI;
    JFrame m_window;
    int m_level;
    
    public
    TSMapperClass()
    {
        // constants
        WIDTH = 30;
        HEIGHT = 30;
        LEVELS = 3;
        OFFSET_X = 5;
        OFFSET_Y = 5;
        OFFSET_L = 1;
        LIGHT_GRAY = new Color( 200, 200, 200 );
        DARK_GRAY = new Color( 220, 220, 220 );
        // globals
        m_level = 0;
        // grid data
        m_grid = new boolean[ LEVELS ][ WIDTH ][ HEIGHT ][ 4 ]; // [ level ][ x ][ y ][ paths{ north, east, south, west } ]
        initGrid( "input.txt" ); // may need to use full path to make it work
        // grid gui
        m_gridGUI = new JPanel();
        m_gridGUI.setLayout( new GridLayout( WIDTH, HEIGHT ));
        updateGridGUI();
        // window
        m_window = new JFrame();
        m_window.addKeyListener( this );
        m_window.setTitle( "LEVEL " + String.valueOf(  m_level - OFFSET_L ));
        m_window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        m_window.getContentPane().add( m_gridGUI );
        m_window.pack();
        m_window.setLocationRelativeTo(null);
        m_window.setVisible(true);
    }
    
    public void
    updateGridGUI()
    {
        // grid GUI
        m_gridGUI.removeAll();
        for( int y = 0; y < HEIGHT; y++ )
        {
            for( int x = 0; x < WIDTH; x++ )
            {
                JPanel p = new JPanel();
                p.setBackground( ( x + y ) % 2 == 0 ? LIGHT_GRAY : DARK_GRAY ); // checkerboard
                p.setBorder( new CustomBorder( m_grid[ m_level ][ x ][ y ] ));
                boolean path = false;
                for( int k = 0; k < 4; k++ ) path = path || m_grid[ m_level ][ x ][ y ][ k ];
                if( !path ) p.setBackground( p.getBackground().darker() );
                
                JLabel coord = new JLabel( String.valueOf( x - OFFSET_X ) + "x" + String.valueOf( y - OFFSET_Y ));
                coord.setForeground( DARK_GRAY.darker() );
                coord.setOpaque( false );
                p.add( coord );
                
                m_gridGUI.add( p );
            }
        }
        m_gridGUI.updateUI();
        m_gridGUI.repaint();
    }
    
    private void
    initGrid( String fileName )
    {
        BufferedReader bf;
        try( FileReader fr = new FileReader( fileName ))
        {
                bf = new BufferedReader( fr );
                String line;
                while( ( line = bf.readLine()) != null )
                {
                    int coordStart = line.indexOf( '[' );
                    int xEnd = line.indexOf( ',', coordStart );
                    int yEnd = line.indexOf(  ',', xEnd + 1 );
                    int zEnd = line.indexOf( ']', yEnd );
                    
                    String sx = line.substring( coordStart + 1, xEnd ).replace( " ", "" );
                    String sy = line.substring( xEnd + 1, yEnd ).replace( " ", "" );
                    String sz = line.substring( yEnd + 1, zEnd ).replace( " ", "" );
                    
                    int x = Integer.valueOf( sx ) + OFFSET_X;
                    int y = Integer.valueOf( sy ) + OFFSET_Y;
                    int z = Integer.valueOf( sz ) + OFFSET_L;
                    
                    boolean[] directions = getDirections( line );
                    
                    for( int k = 0; k < 4; k++ ) m_grid[ z ][ x ][ y ][ k ] = directions[ k ];
                }
                bf.close();
        } catch( Exception ex ) { ex.printStackTrace(); }
    }
    
    private boolean[]
    getDirections( String text )
    {
        boolean[] d = new boolean[ 4 ]; // { north, east, south, west }
        for( int k = 0; k < 4; k++ ) d[ k ] = text.contains( DIRECT[ k ] );
        return d;
    }

    @Override
    public void keyTyped( KeyEvent e )
    {
        
    }

    @Override
    public void keyPressed( KeyEvent e )
    {
    }

    @Override
    public void keyReleased( KeyEvent e )
    {
        int key = e.getKeyCode();
        if( key == KeyEvent.VK_RIGHT || key == KeyEvent.VK_LEFT )
        {
            if( key == KeyEvent.VK_RIGHT ) m_level = ( m_level + 1 ) % LEVELS;
            if( key == KeyEvent.VK_LEFT ) m_level--;
            if( m_level < 0 ) m_level += LEVELS;
            updateGridGUI();
            m_window.setTitle( "LEVEL " + String.valueOf(  m_level - OFFSET_L ));
            m_window.repaint();
        }
    }
}

class CustomBorder extends AbstractBorder
{
    private boolean[] m_directions;
    
    public
    CustomBorder( boolean[] d )
    {
        m_directions = d;
    }
    
    @Override public void
    paintBorder( Component c, Graphics g, int x, int y, int width, int height)
    {
        super.paintBorder( c, g, x, y, width, height );
        for( int k = 0; k < 4; k++ )
        {
            // draw border
            if( !m_directions[ k ] )
            {
                int sX, eX, sY, eY;
                if( k % 2 == 0 ) // NORTH or SOUTH
                {
                    sX = 0;
                    eX = width;
                    sY = eY = Math.min( k, 1 ) * height;
                }
                else // EAST or WEST
                {
                    sX = eX = Math.min( ( k + 1 ) % 4, 1 ) * width;
                    sY = 0;
                    eY = height;
                }
                g.setColor( Color.DARK_GRAY );
                if( k == 1 || k == 2 )  g.fillRect( sX - 2, sY - 2, eX, eY );
                else                    g.fillRect( sX, sY, eX + 2, eY + 2 );
            }
        }
    }
}
