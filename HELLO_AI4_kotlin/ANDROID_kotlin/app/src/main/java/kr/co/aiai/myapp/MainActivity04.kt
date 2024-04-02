package kr.co.aiai.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import java.util.Collections

class MainActivity04 : AppCompatActivity() {

    lateinit var tv1 : TextView
    lateinit var tv2 : TextView
    lateinit var tv3 : TextView
    lateinit var tv4 : TextView
    lateinit var tv5 : TextView
    lateinit var tv6 : TextView
    lateinit var test : TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main04)
        val btn = findViewById<Button>(R.id.btn)
        tv1 = findViewById(R.id.tv1)
        tv2 = findViewById(R.id.tv2)
        tv3 = findViewById(R.id.tv3)
        tv4 = findViewById(R.id.tv4)
        tv5 = findViewById(R.id.tv5)
        tv6 = findViewById(R.id.tv6)
        test = findViewById(R.id.test)

        btn.setOnClickListener(){
            myClick()
        }
    }

    fun myClick(){
        var happy = mutableListOf<Int>()
        var view : Array<TextView> = arrayOf(tv1,tv2,tv3,tv4,tv5,tv6)
        var i : Int = 0
        while(happy.size < 6){
            var ran:Int = (Math.random()*45+1).toInt();
            if(ran !in happy ){
                happy.add(i,ran)
                i++
            }
        }
        happy.sort()
        for( k : Int in 0..5){
//            Log.d("mine",happy[k].toString())
            view.get(k).setText(happy.get(k).toString())
        }
    }
}