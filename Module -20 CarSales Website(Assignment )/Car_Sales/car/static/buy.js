document.getElementById('Buy').addEventListener('click', function()
{
    console.log('buy now Ok');
    const quantitys =document.getElementById('quantity')
    let quantityValue=quantitys.innerText
    const quantityInt=parseInt(quantityValue)
    document.getElementById('quantity').innerText=quantityInt-1

})