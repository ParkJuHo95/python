package kr.co.aiai.high;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Matrix;
import android.graphics.Paint;
import android.os.Bundle;
import android.view.View;

public class ActivityPaint extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(new ViewMe(this));
    }

    class ViewMe extends View {

        public ViewMe(Context context) {
            super(context);
        }

        @Override
        protected void onDraw(Canvas canvas) {
            Paint paint = new Paint();
            paint.setStrokeWidth(10);

            // paint.setAlpha(125);

//            Matrix matrix = new Matrix();
//            matrix.postRotate(45, 100, 100);
//            canvas.setMatrix(matrix);
//            String txt = "Hello Graphic";
//            canvas.drawText(txt, 5, txt.length(), 100, 100, paint);
//            canvas.drawRect(0,0,100,200,paint);
            paint.setColor(Color.RED);
            canvas.drawLine(20,10,200,10,paint);
            paint.setColor(Color.rgb(255,120,0));
            canvas.drawLine(20,100,200,100,paint);
            paint.setColor(Color.rgb(255,255,0));
            canvas.drawLine(20,200,200,200,paint);
            paint.setColor(Color.rgb(0,255,0));
            canvas.drawLine(20,300,200,300,paint);
            paint.setColor(Color.rgb(0,0,255));
            canvas.drawLine(20,400,200,400,paint);
            paint.setColor(Color.rgb(0,0,180));
            canvas.drawLine(20,500,200,500,paint);
            paint.setColor(Color.rgb(180,0,180));
            canvas.drawLine(20,600,200,600,paint);

            super.onDraw(canvas);

        }
    }
}